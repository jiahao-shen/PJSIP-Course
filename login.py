"""
@project: PJSIP-Lab
@author: sam
@file login.py
@ide: PyCharm
@time: 2019-11-25 12:36:37
@blog: https://jiahaoplus.com
"""
import tkinter as tk
import pjsua2 as pj
from account import Account
from main import Main
from config import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg


class Login(tk.Tk):
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

        """
        Account information
        """
        self.domain = tk.StringVar(value=default_domain)
        self.username = tk.StringVar(value='1001')
        self.password = tk.StringVar(value='1001')

        """
        Initialize UI
        """
        self.title('Login')
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth() / 2),
                                      int(self.winfo_screenheight() / 2)))

        self.photo = ImageTk.PhotoImage(Image.open('image/phone.png'))
        tk.Label(self, image=self.photo).grid(column=0, rowspan=3,
                                              ipadx=10, ipady=10)

        tk.Label(self, text='SIP Account Setup', font=title_font).grid(
            row=0, column=1, columnspan=2, sticky=tk.W)
        tk.Label(self, text='Enter account details', font=content_font).grid(
            row=1, column=1, columnspan=2, sticky=tk.W)

        tk.Label(self, text='Domain', font=content_font).grid(row=2, column=1)
        tk.Entry(self, textvariable=self.domain, justify='center',
                 font=content_font).grid(row=2, column=2, padx=5, pady=5)

        tk.Label(self, text='UserName', font=content_font).grid(row=3,
                                                                column=1)
        tk.Entry(self, textvariable=self.username, justify='center',
                 font=content_font).grid(row=3, column=2, padx=5, pady=5)

        tk.Label(self, text='Password', font=content_font).grid(row=4,
                                                                column=1)
        tk.Entry(self, textvariable=self.password, show='*', justify='center',
                 font=content_font).grid(row=4, column=2, padx=5, pady=5)

        tk.Button(self, text='OK', command=self.on_ok, font=content_font,
                  width=10).grid(row=5, column=1, padx=5, pady=20)
        tk.Button(self, text='Cancel', command=self.on_exit, font=content_font,
                  width=10).grid(row=5, column=2, padx=5, pady=20)
        
        self.mainloop()

    def on_ok(self):
        errors = ''
        if not self.domain.get():
            errors += 'Domain is required\n'
        if not self.username.get():
            errors += 'Username is required\n'
        if not self.password.get():
            errors += 'Password is required\n'

        if not self.ep.utilVerifySipUri('sip:' + self.username.get() + '@' +
                                        self.domain.get()) == pj.PJ_SUCCESS:
            errors += 'Invalid SIP URI\n'

        if errors:
            self.show_error(errors)
            return

        acc_cfg = pj.AccountConfig()
        acc_cfg.idUri = 'sip:' + self.username.get() + '@' + self.domain.get()
        acc_cfg.regConfig.registrarUri = 'sip:' + self.domain.get()
        acc_cfg.regConfig.registerOnAdd = True
        acc_cfg.sipConfig.authCreds.append(
            pj.AuthCredInfo('digest', '*', self.username.get(),
                            pj.PJSIP_CRED_DATA_PLAIN_PASSWD,
                            self.password.get()))

        self.destroy()
        Main(self.ep, acc_cfg)

    def on_exit(self):
        self.ep.libDestroy()
        self.destroy()

    def show_error(self, content):
        msg.showerror('Error Detected', content)


if __name__ == '__main__':
    Login()
