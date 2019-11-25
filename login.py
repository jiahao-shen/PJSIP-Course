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
from main import Main
from config import *
from PIL import Image, ImageTk
from tkinter import messagebox as msg


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        # Set title
        self.title('Login')
        # Set location
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth() / 2),
                                      int(self.winfo_screenheight() / 2)))

        # PJSUA2 Endpoint initialize
        self.ep = pj.Endpoint()
        self.ep.libCreate()

        # The account information
        self.domain = tk.StringVar(value=default_domain)
        self.username = tk.StringVar()
        self.password = tk.StringVar()

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
            msg.showerror('Error detected:', errors)
            return
        else:
            self.destroy()
            Main(self.ep)

    def on_exit(self):
        self.destroy()


if __name__ == '__main__':
    login = Login()
