"""
@project: PJSIP-Lab
@author: sam
@file main.py
@ide: PyCharm
@time: 2019-11-24 21:36:37
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj
import tkinter as tk
from account import Account


class Main(tk.Tk):
    def __init__(self, ep, acc_cfg):
        super().__init__()

        """
        Initialize PJSUA2
        """
        self.ep = ep
        self.acc_cfg = acc_cfg

        self.acc = Account(self)
        self.acc.create(self.acc_cfg)
        """
        Initialize UI
        """
        self.title(self.acc_cfg.idUri)
        self.geometry('+{}+{}'.format(int(self.winfo_screenwidth() / 2),
                                      int(self.winfo_screenheight() / 2)))

        self.mainloop()
