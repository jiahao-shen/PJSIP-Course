"""
@project: PJSIP-Lab
@author: sam
@file chat.py
@ide: Visual Studio Code
@time: 2019-12-03 17:42:37
@blog: https://jiahaoplus.com
"""
import time
import pjsua2 as pj
import tkinter as tk
from config import *
from call import Call
from tkinter import ttk
from buddy import Buddy
from account import Account


class ChatDialog(tk.Toplevel):

    def __init__(self, acc, bud):
        tk.Toplevel.__init__(self)
        self.acc = acc
        self.bud = bud

        self.call = Call(self.acc, self.bud.cfg.uri, self)
        self.call_prm = pj.CallOpParam()

        self.message = tk.StringVar()
        self.state = tk.StringVar()
        self.cnt = 0

        self.hold = False

        """
        Initialize UI
        """
        self.title(bud.cfg.uri)
        self.resizable(width=False, height=False)
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth() / 2),
                                      int(self.winfo_screenheight() / 2)))

        self.chart = tk.Text(self, width=40, height=25, font=CONTENT)
        self.chart.config(state=tk.DISABLED)
        self.chart.grid(row=0, column=0, rowspan=10,
                        columnspan=2, padx=10, pady=10)

        self.scrl = ttk.Scrollbar(self, orient=tk.VERTICAL,
                                  command=self.chart.yview)
        self.chart.config(yscrollcommand=self.scrl.set)
        self.scrl.grid(row=0, column=2, rowspan=10, sticky='nsw')

        self.type_entry = tk.Entry(self, textvariable=self.message,
                                   font=CONTENT, width=30)
        self.type_entry.bind('<Return>', self._send_message)
        self.type_entry.grid(row=10, column=0, padx=10, pady=10)

        tk.Button(self, text='Call', font=CONTENT, width=10,
                  command=self._makecall).grid(row=10, column=1, padx=2, pady=2)

        tk.Label(self, textvariable=self.state, font=TITLE).grid(
            row=5, column=3, columnspan=3, padx=10, pady=10)
        self.timer = tk.Label(self, font=CONTENT).grid(
            row=6, column=3, columnspan=3, padx=10, pady=10)

        tk.Button(self, text='Speaker', font=CONTENT, width=10,
                  command=self._speaker).grid(row=8, column=3, padx=10, pady=10)
        tk.Button(self, text='Microphone', font=CONTENT, width=10,
                  command=self._microphone).grid(row=8, column=5, padx=10, pady=10)
        tk.Button(self, text='Hold', font=CONTENT, width=10,
                  command=self._sethold).grid(row=9, column=3, padx=10, pady=10)
        tk.Button(self, text='Hangup', font=CONTENT, width=10,
                  command=self._hangup).grid(row=9, column=5, padx=10, pady=10)

    def add_message(self, msg):
        self.chart.config(state=tk.NORMAL)
        self.chart.insert(tk.END, time.strftime(
            '%Y-%m-%d %H:%M:%S\n', time.localtime()))
        self.chart.insert(tk.END, msg + '\r\n')
        self.chart.config(state=tk.DISABLED)
        self.chart.yview(tk.END)
        pj.PJSIP_INV_STATE_CALLING

    def is_calling(self):
        self.state.set('Calling...')

    def is_connect(self):
        self.state.set('Connect')

    def is_disconnect(self):
        self.state.set('Disconnect')

    def is_holding(self):
        self.state.set('Holding...')

    def _speaker(self):
        pass

    def _microphone(self):
        pass

    def _send_message(self, event):
        if self.message.get() != '':
            self.add_message('me: ' + self.message.get())
            self.message.set('')

    def _makecall(self):
        # self.call.makeCall(self.bud.cfg.uri, self.call_prm)
        self._count_down()

    def _sethold(self):
        if not self.hold:
            self.call.setHold(self.call_prm)
            self.hold = True
            self.is_holding()
        else:
            self.call_prm.opt.flag = pj.PJSUA_CALL_UNHOLD
            self.call.reinvite(self.call_prm)
            self.hold = False
            self.is_connect()

    def _hangup(self):
        self.call.hangup(self.call_prm)

    def _count_down(self):
        self.cnt += 1
        second = self.cnt % 60
        minute = self.cnt // 60
        hour = self.cnt // 3600
        print(hour, minute, second)
        # self.timer['text'] = str(hour) + ':' + str(minute) + ':' + str(second)
        self.after(1000, self._count_down)

def test():
    acc = Account(None)

    bud = Buddy(None, '1002')
    bud_cfg = pj.BuddyConfig()
    bud_cfg.uri = 'sip:1002@27.102.107.237'

    ChatDialog(acc, bud).mainloop()


if __name__ == '__main__':
    test()
