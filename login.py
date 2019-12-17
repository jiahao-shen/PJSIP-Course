"""
@project: PJSIP-Lab
@author: sam
@file login.py
@ide: Visual Studio Code
@time: 2019-11-25 12:36:37
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj
import tkinter as tk


from utils import *
from config import *
from endpoint import *
from tkinter import messagebox as msg


class Login(tk.Toplevel):

    def __init__(self, parent, cfg):
        tk.Toplevel.__init__(self, parent)
        self.transient(parent)
        self.parent = parent
        self.cfg = cfg

        """
        Account Information
        """
        self.domain = tk.StringVar(value=DEFAULT_DOMAIN)
        self.username = tk.StringVar(value=DEFAULT_USERNAME)
        self.password = tk.StringVar(value=DEFAULT_USERNAME)
        self.is_ok = False

        """
        Initialize UI
        """
        self.title('Login')
        self.resizable(width=False, height=False)
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth() / 2),
                                      int(self.winfo_screenheight() / 2)))

        self.photo = tk.PhotoImage(file='image/phone.png')
        tk.Label(self, image=self.photo).grid(column=0, rowspan=3,
                                              padx=5, pady=5)

        tk.Label(self, text='SIP Account Setup', font=FONT_TITLE).grid(
            row=0, column=1, rowspan=2, columnspan=2, padx=5, pady=5)

        tk.Label(self, text='Domain', font=FONT_CONTENT).grid(row=2, column=1)
        tk.Entry(self, textvariable=self.domain, justify='center',
                 font=FONT_CONTENT).grid(row=2, column=2, padx=5, pady=5)

        tk.Label(self, text='UserName', font=FONT_CONTENT).grid(row=3, column=1)
        tk.Entry(self, textvariable=self.username, justify='center',
                 font=FONT_CONTENT).grid(row=3, column=2, padx=5, pady=5)

        tk.Label(self, text='Password', font=FONT_CONTENT).grid(row=4, column=1)
        tk.Entry(self, textvariable=self.password, show='*', justify='center',
                 font=FONT_CONTENT).grid(row=4, column=2, padx=5, pady=5)

        tk.Button(self, text='Login', font=FONT_CONTENT, width=10,
                  command=self._login).grid(row=5, column=1, padx=5, pady=20)
        tk.Button(self, text='Exit', font=FONT_CONTENT, width=10,
                  command=self._exit).grid(row=5, column=2, padx=5, pady=20)

    def _login(self):
        errors = ''
        if not self.domain.get():
            errors += 'Domain is required\n'
        if not self.username.get():
            errors += 'Username is required\n'
        if not self.password.get():
            errors += 'Password is required\n'
        if not validateSipUri('sip:' + self.username.get() + '@' + self.domain.get()):
            errors += 'Invalid SIP URI\n'

        if errors:
            msg.showerror('Error Detected', errors)
            return

        self.cfg.idUri = 'sip:' + self.username.get() + '@' + self.domain.get()
        self.cfg.regConfig.registrarUri = 'sip:' + self.domain.get()
        self.cfg.regConfig.registerOnAdd = True
        self.cfg.sipConfig.authCreds.append(pj.AuthCredInfo(
            'digest', '*', self.username.get(), pj.PJSIP_CRED_DATA_PLAIN_PASSWD, self.password.get()))

        # Video support
        self.cfg.videoConfig.autoTransmitOutgoing = True
        self.cfg.videoConfig.defaultCaptureDevice = pj.PJMEDIA_VID_DEFAULT_CAPTURE_DEV
        self.cfg.videoConfig.defaultRenderDevice = pj.PJMEDIA_VID_DEFAULT_RENDER_DEV

        self.is_ok = True
        self.destroy()

    def _exit(self):
        self.destroy()

    def do_modal(self):
        if self.parent:
            self.parent.wait_window(self)
        else:
            self.wait_window(self)
        return self.is_ok
