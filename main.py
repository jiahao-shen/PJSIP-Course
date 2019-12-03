"""
@project: PJSIP-Lab
@author: sam
@file main.py
@ide: Visual Studio Code
@time: 2019-11-24 21:36:37
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj
import tkinter as tk

from config import *
from tkinter import ttk
from buddy import Buddy
from account import Account
from chat import ChatDialog
from login import LoginDialog
from tkinter import messagebox as msg


class Main(tk.Tk):

    def __init__(self):
        super().__init__()

        """
        Initialize PJSUA2
        """
        self.ep = pj.Endpoint()
        self.ep.libCreate()

        self.ep_cfg = pj.EpConfig()
        self.ep_cfg.uaConfig.threadCnt = 0
        self.ep_cfg.logConfig.level = 1

        self.ep.libInit(self.ep_cfg)

        self.sip_cfg = pj.TransportConfig()
        self.ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, self.sip_cfg)
        self.ep.libStart()

        self.acc = None
        self.acc_cfg = pj.AccountConfig()

        self.domain = DEFAULT_DOMAIN

        """
        Initialize Buddy
        """
        self.input = tk.StringVar()
        self.buddy_list = {}

        """
        Initialize UI
        """
        self.title('SIP Client')
        self.resizable(width=False, height=False)
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth() / 2),
                                      int(self.winfo_screenheight() / 2)))

        self.buddy_entry = tk.Entry(self, textvariable=self.input, 
                                    font=CONTENT, width=30)
        self.buddy_entry.grid(row=0, column=0, columnspan=10, padx=10, pady=10)
        self.buddy_entry.bind('<Return>', self._add_buddy)

        self.buddy_view = ttk.Treeview(self, column=['1', '2'], show='headings', 
                                       selectmode='browse')
        self.buddy_view.column('1', width=80, anchor='center')
        self.buddy_view.column('2', width=200, anchor='center')
        self.buddy_view.heading('1', text='Buddies')
        self.buddy_view.heading('2', text='Status')
        self.buddy_view.grid(row=1, column=0, columnspan=10, padx=10, pady=10)
        self.buddy_view.bind('<Double-Button-1>', self._create_chat)
        self.buddy_view.bind('<BackSpace>', self._delete_buddy)

        tk.Button(self, text='Logout', font=CONTENT, width=8,
                  command=self._login).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self, text='Exit', font=CONTENT, width=8,
                  command=self._exit).grid(row=2, column=8, padx=10, pady=10)

        self._login()

        self.mainloop()

    def _add_buddy(self, event):
        iid = self.input.get()
        if not self.buddy_view.exists(iid):
            bud = Buddy(self, iid) 
            bud_cfg = pj.BuddyConfig()
            bud_cfg.uri = 'sip:' + iid + '@' + self.domain
            bud_cfg.subscribe = True
            bud.create(self.acc, bud_cfg)

            self.buddy_list[iid] = bud
            self.update_buddy(bud)
        
        self.input.set('')

    def _create_chat(self, event):
        for item in self.buddy_view.selection():
            ChatDialog(self.acc, self.buddy_list[item])

    def _delete_buddy(self, event):
        for item in self.buddy_view.selection():
            self.buddy_view.delete(item)
            self.buddy_list.pop(item)

    def _login(self):
        dlg = LoginDialog(self, self.ep, self.acc_cfg)
        if dlg.do_modal():
            self.acc = Account(self)
            self.acc.create(self.acc_cfg)
            self.title(self.acc_cfg.idUri)
            self.domain = self.acc_cfg.regConfig.registrarUri.split(':')[1]

        if self.acc is None:
            self._exit()

    def _exit(self):
        self.ep.libDestroy()
        self.ep = None
        self.destroy()

    def update_buddy(self, bud):
        iid = bud.iid
        if self.buddy_view.exists(iid):
            self.buddy_view.item(iid, value=(iid, bud.status_text()))
        else:
            self.buddy_view.insert('', 'end', iid=iid, values=(iid, bud.status_text()))


if __name__ == '__main__':
    Main()
