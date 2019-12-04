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


class ChatDialog(tk.Toplevel):

    def __init__(self, acc, bud):
        tk.Toplevel.__init__(self)
        self.acc = acc
        self.bud = bud

        self.call = Call(self.acc, self.bud.cfg.uri, self)
        self.call_prm = pj.CallOpParam()
        self.call_prm.opt.audioCount = 1

        self.message = tk.StringVar()

        """
        Initialize UI
        """
        self.title(bud.cfg.uri)
        self.resizable(width=False, height=False)
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth() / 2),
                                      int(self.winfo_screenheight() / 2)))

        self.chart = tk.Text(self, width=40, height=25, font=CONTENT)
        self.chart.config(state=tk.DISABLED)
        self.chart.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.scrl = ttk.Scrollbar(self, orient=tk.VERTICAL,
                                  command=self.chart.yview)
        self.chart.config(yscrollcommand=self.scrl.set)
        self.scrl.grid(row=0, column=3, sticky='nsw')

        self.type_entry = tk.Entry(self, textvariable=self.message,
                                   font=CONTENT, width=40)
        self.type_entry.bind('<Return>', self._send_message)
        self.type_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        tk.Button(self, text='Call', font=CONTENT, width=10,
                  command=self._call).grid(row=2, column=0, padx=5, pady=5)

        tk.Button(self, text='Hold', font=CONTENT, width=10,
                  command=self._hold).grid(row=2, column=1, padx=5, pady=5)

        tk.Button(self, text='Hangup', font=CONTENT, width=10,
                  command=self._hangup).grid(row=2, column=2, padx=5, pady=5)

    def add_message(self, msg):
        self.chart.config(state=tk.NORMAL)
        self.chart.insert(tk.END, time.strftime(
            '%Y-%m-%d %H:%M:%S\n', time.localtime()))
        self.chart.insert(tk.END, msg + '\r\n')
        self.chart.config(state=tk.DISABLED)
        self.chart.yview(tk.END)

    def _send_message(self, event):
        if self.message.get() != '':
            self.add_message('me: ' + self.message.get())
            self.message.set('')

    def _call(self):
        self.call.makeCall(self.bud.cfg.uri, self.call_prm)

    def _hold(self):
        self.call.setHold(self.call_prm)

    def _hangup(self):
        self.call.hangup(self.call_prm)
