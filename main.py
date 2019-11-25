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


class Main(tk.Tk):
    def __init__(self, ep):
        super().__init__()
        self.title('Main')
        self.ep = ep

        self.ep_cfg = pj.EpConfig()
        self.ep.libInit(self.ep_cfg)

        self.mainloop()
