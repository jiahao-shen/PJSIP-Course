"""
@project: PJSIP-Lab
@author: sam
@file chat.py
@ide: Visual Studio Code
@time: 2019-12-03 17:42:37
@blog: https://jiahaoplus.com
"""
import time
import random
import pjsua2 as pj
import tkinter as tk

from utils import *
from config import *
from call import Call
from tkinter import ttk
from buddy import Buddy
from account import Account
from endpoint import Endpoint


class ChatDialog(tk.Toplevel):

    def __init__(self, acc, bud, app):
        tk.Toplevel.__init__(self)
        self.acc = acc
        self.bud = bud
        self.app = app

        self.call = None
        self.state = AudioState.DISCONNECT

        """
        Initialize UI
        """
        self.photo = tk.PhotoImage(file='image/user.png')

        self.title(bud.cfg.uri)
        self.resizable(width=False, height=False)
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth() / 2),
                                      int(self.winfo_screenheight() / 2)))

        self.canvas = tk.Canvas(
            self, width=400, height=400, bg=COLOR_BACKGROUND)
        self.canvas.grid(row=0, column=0, rowspan=10, columnspan=2,
                         padx=10, pady=10, sticky='nsew')
        self.chat = tk.Frame(self.canvas)
        self.canvas.create_window(
            (0, 0), window=self.chat, anchor='nw', tags='chat')
        self.canvas.bind('<Configure>', self._canvas_resize)
        self.chat.bind('<Configure>', self._chat_resize)

        self.scrl = ttk.Scrollbar(self, orient=tk.VERTICAL,
                                  command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.scrl.set)
        self.scrl.grid(row=0, column=2, rowspan=10, sticky='nsw')

        # Message Entry
        self.message = tk.Entry(self, font=FONT_CONTENT, width=30)
        self.message.bind('<Return>', self._send_message)
        self.message.grid(row=10, column=0, padx=10, pady=10)

        # Call Button
        tk.Button(self, text='Call', font=FONT_CONTENT, width=10,
                  command=self._make_call).grid(row=10, column=1, padx=2, pady=2)

        # State Label
        self.state_label = tk.Label(self, font=FONT_TITLE)
        self.state_label.grid(
            row=5, column=3, columnspan=3, padx=10, pady=10)

        # Timer Label
        self.timer = StopWatch(self)
        self.timer.grid(row=6, column=3, columnspan=3, padx=10, pady=10)

        # RX Volume Scale
        tk.Label(self, text='Micphone', font=FONT_CONTENT).grid(
            row=7, column=3, padx=10, pady=10)
        self.rx_scale = tk.Scale(
            self, from_=0.0, to=10.0, orient=tk.HORIZONTAL, showvalue=0)
        self.rx_scale.set(5.0)
        self.rx_scale.bind('<ButtonRelease-1>', self._rx_volume)
        self.rx_scale.grid(row=7, column=4, columnspan=2, padx=5, pady=5)

        # TX Volume Scale
        tk.Label(self, text='Speaker', font=FONT_CONTENT).grid(
            row=8, column=3, padx=10, pady=10)
        self.tx_scale = tk.Scale(
            self, from_=0.0, to=10.0, orient=tk.HORIZONTAL, showvalue=0)
        self.tx_scale.set(5.0)
        self.tx_scale.bind('<ButtonRelease-1>', self._tx_volume)
        self.tx_scale.grid(row=8, column=4, columnspan=2, padx=5, pady=5)

        # Hold Button
        self.hold_button = tk.Button(
            self, text='Hold', font=FONT_CONTENT, width=10, command=self._set_hold)
        self.hold_button.grid(row=9, column=3, padx=10, pady=10)

        # Hangup Button
        tk.Button(self, text='Hangup', font=FONT_CONTENT, width=10,
                  command=self._hang_up).grid(row=9, column=5, padx=10, pady=10)

        self.protocol('WM_DELETE_WINDOW', self._exit)

    def add_message(self, msg, flag):
        tk.Label(self.chat, text=time.strftime(
            '%H:%M:%S', time.localtime()), fg=COLOR_TIME).pack(anchor='center')
        if flag == MessageState.SEND or MessageState.INFO:
            content = tk.Frame(self.chat)
            tk.Label(content, image=self.photo).pack(side=tk.RIGHT, anchor='n')
            tk.Label(content, font=FONT_MESSAGE, text=msg, wraplength=200,
                     justify='left', bg=COLOR_SEND_BUBBLE).pack(side=tk.RIGHT, ipadx=5, ipady=5)
            content.pack(anchor='e')
        elif flag == MessageState.RECEIVE:
            content = tk.Frame(self.chat)
            tk.Label(content, image=self.photo).pack(side=tk.LEFT, anchor='n')
            tk.Label(content, font=FONT_MESSAGE, text=msg, wraplength=200, justify='left',
                     bg=COLOR_RECEIVE_BUBBLE).pack(side=tk.LEFT, ipadx=5, ipady=5)
            content.pack(anchor='w')

        # Important!!! Can't remove!!!
        self.chat.update_idletasks()
        self.canvas.yview_moveto(1)

    def is_calling(self):
        self.state = AudioState.CALLING
        self.state_label['text'] = self.state.value

    def is_connect(self):
        self.state = AudioState.CONNECT
        self.state_label['text'] = self.state.value
        self.timer.reset()
        self.timer.start()

    def is_disconnect(self):
        self.state = AudioState.DISCONNECT
        self.state_label['text'] = self.state.value
        self.timer.stop()
        self.add_message('Call Ended\nLast ' + self.timer.get(), MessageState.INFO)

    def is_hold(self):
        self.state = AudioState.HOLD
        self.state_label['text'] = self.state.value
        self.timer.stop()

    def is_unhold(self):
        self.state = AudioState.CONNECT
        self.state_label['text'] = self.state.value
        self.timer.start()

    def _send_message(self, event):
        msg = self.message.get()
        if msg != '':
            msg_prm = pj.SendInstantMessageParam()
            msg_prm.content = msg
            self.bud.sendInstantMessage(msg_prm)

            self.add_message(msg, MessageState.SEND)
            self.message.delete(0, 'end')

    def receive_message(self, msg):
        self.add_message(msg, MessageState.RECEIVE)

    def _make_call(self):
        if self.state == AudioState.DISCONNECT:
            # Initialize Call
            self.call = Call(self.acc, self.bud.cfg.uri, self)
            # Create paramter
            call_prm = pj.CallOpParam()
            # Important!!! Can't remove!!!
            call_prm.opt.audioCount = 1
            # Make call
            self.call.makeCall(self.bud.cfg.uri, call_prm)

    def receive_call(self, call):
        # Update call and set chat
        self.call = call
        self.call.chat = self
        # Receive call
        call_prm = pj.CallOpParam()
        call_prm.statusCode = pj.PJSIP_SC_OK
        self.call.answer(call_prm)

    def _set_hold(self):
        if self.call is not None:
            call_prm = pj.CallOpParam()
            if self.state == AudioState.CONNECT:
                self.call.setHold(call_prm)
                self.hold_button['text'] = 'UnHold'
                self.is_hold()
            elif self.state == AudioState.HOLD:
                # Important!!! Can't remove!!!
                call_prm.opt.audioCount = 1
                call_prm.opt.flag = pj.PJSUA_CALL_UNHOLD
                self.call.reinvite(call_prm)
                self.hold_button['text'] = 'Hold'
                self.is_unhold()
        else:
            print('Call isn\'t initialized')

    def _hang_up(self):
        if self.call is not None:
            call_prm = pj.CallOpParam()
            if self.state != AudioState.DISCONNECT:
                self.call.hangup(call_prm)

    def _rx_volume(self, event):
        am = self.call.getAudioMedia(-1)
        am.adjustRxLevel(self.rx_scale.get() / 10.0)
        

    def _tx_volume(self, event):
        am = self.call.getAudioMedia(-1)
        am.adjustTxLevel(self.tx_scale.get() / 10.0)

    def _canvas_resize(self, event):
        # Important!!! Can't remove!!!
        self.canvas.itemconfig('chat', width=event.width)

    def _chat_resize(self, event):
        # Important!!! Can't remove!!!
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def _exit(self):
        try:
            self.app.delete_chat(self.bud.iid)
            self._hang_up()
            self.destroy()
        except:
            self.destroy()


class StopWatch(tk.Frame):
    """ Implements a stop watch frame widget. """

    def __init__(self, parent=None, **kw):
        tk.Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = tk.StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        """ Make the time label. """
        l = tk.Label(self, textvariable=self.timestr, font=FONT_TITLE)
        self._setTime(self._elapsedtime)
        l.pack(fill=tk.X, expand=tk.NO, pady=2, padx=2)

    def _update(self):
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap / 60)
        seconds = int(elap - minutes * 60.0)
        hseconds = int((elap - minutes * 60.0 - seconds) * 100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))

    def start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def stop(self):
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def reset(self):
        """ Reset the stopwatch. """
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

    def get(self):
        return self.timestr.get()

def test():
    root = tk.Tk()

    acc = Account(None)
    bud = Buddy(None, '1002')
    bud_cfg = pj.BuddyConfig()
    bud_cfg.uri = 'sip:1002@27.102.107.237'

    ChatDialog(acc, bud, root)
    root.mainloop()


if __name__ == '__main__':
    test()
