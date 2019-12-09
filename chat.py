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

    def __init__(self, acc, bud):
        tk.Toplevel.__init__(self)
        self.acc = acc
        self.bud = bud

        self.call = Call(self.acc, self.bud.cfg.uri, self)
        self.call_prm = pj.CallOpParam()
        # Important!!! Can't remove!!!
        self.call_prm.opt.audioCount = 1

        self.message = tk.StringVar()
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
        self.message_entry = tk.Entry(
            self, textvariable=self.message, font=FONT_CONTENT, width=30)
        self.message_entry.bind('<Return>', self._send_message)
        self.message_entry.grid(row=10, column=0, padx=10, pady=10)

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

        # Hold Button
        self.hold_button = tk.Button(
            self, text='Hold', font=FONT_CONTENT, width=10, command=self._set_hold)
        self.hold_button.grid(row=9, column=3, padx=10, pady=10)

        # Hangup Button
        tk.Button(self, text='Hangup', font=FONT_CONTENT, width=10,
                  command=self._hang_up).grid(row=9, column=5, padx=10, pady=10)

    def add_message(self, msg, flag):
        tk.Label(self.chat, text=time.strftime(
            '%H:%M:%S', time.localtime()), fg=COLOR_TIME).pack(anchor='center')
        if flag == MessageState.SEND:
            content = tk.Frame(self.chat)
            tk.Label(content, image=self.photo).pack(side=tk.RIGHT, anchor='n')
            tk.Label(content, font=FONT_MESSAGE, text=msg, wraplength=200,
                     justify='left', bg=COLOR_SEND_BUBBLE).pack(side=tk.RIGHT)
            content.pack(anchor='e')
        elif flag == MessageState.RECEIVE:
            content = tk.Frame(self.chat)
            tk.Label(content, image=self.photo).pack(side=tk.LEFT, anchor='n')
            tk.Label(content, font=FONT_MESSAGE, text=msg, wraplength=200,
                     justify='left', bg=COLOR_RECEIVE_BUBBLE).pack(side=tk.LEFT)
            content.pack(anchor='w')
        elif flag == MessageState.INFO:
            pass

        # Important!!! Can't remove!!!
        self.chat.update_idletasks()
        self.canvas.yview_moveto(1)

    def is_calling(self):
        self.state = AudioState.CALLING
        self.state_label['text'] = self.state.value

    def is_connect(self):
        self.state = AudioState.CONNECT
        self.state_label['text'] = self.state.value
        self.timer.Reset()
        self.timer.Start()

    def is_disconnect(self):
        self.state = AudioState.DISCONNECT
        self.state_label['text'] = self.state.value
        self.timer.Stop()

    def is_holding(self):
        self.state = AudioState.HOLD
        self.state_label['text'] = self.state.value
        self.timer.Stop()

    def _send_message(self, event):
        if self.message.get() != '':
            if random.random() > 0.5:
                self.add_message(self.message.get(), MessageState.SEND)
            else:
                self.add_message(self.message.get(), MessageState.RECEIVE)
            self.message.set('')

    def receive_messgae(self, msg):
        pass
        # self.add_message(msg)

    def _make_call(self):
        if self.state == AudioState.DISCONNECT:
            self.call.makeCall(self.bud.cfg.uri, self.call_prm)

    def _set_hold(self):
        if self.state == AudioState.CONNECT:
            self.call.setHold(self.call_prm)
            self.hold_button['text'] = 'UnHold'
            self.is_holding()
        elif self.state == AudioState.HOLD:
            # Important!!! Can't remove!!!
            self.call_prm.opt.audioCount = 1
            self.call_prm.opt.flag = pj.PJSUA_CALL_UNHOLD
            self.call.reinvite(self.call_prm)
            self.hold_button['text'] = 'Hold'
            self.is_connect()

    def _hang_up(self):
        if self.state == AudioState.CONNECT or self.state == AudioState.HOLD:
            self.call.hangup(self.call_prm)

    def _canvas_resize(self, event):
        # Important!!! Can't remove!!!
        self.canvas.itemconfig('chat', width=event.width)

    def _chat_resize(self, event):
        # Important!!! Can't remove!!!
        self.canvas.config(scrollregion=self.canvas.bbox('all'))


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
        l = tk.Label(self, textvariable=self.timestr, font=FONT_CONTENT)
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

    def Start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1

    def Stop(self):
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):
        """ Reset the stopwatch. """
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)


def test():
    acc = Account(None)

    bud = Buddy(None, '1002')
    bud_cfg = pj.BuddyConfig()
    bud_cfg.uri = 'sip:1002@27.102.107.237'

    ChatDialog(acc, bud).mainloop()


if __name__ == '__main__':
    test()
