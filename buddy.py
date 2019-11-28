"""
@project: PJSIP-Lab
@author: sam
@file buddy.py
@ide: PyCharm
@time: 2019-11-27 21:36:37
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj 


class Buddy(pj.Buddy):
    def __init__(self):
        super().__init__()

    def onBuddyState(self):
        buddy_info = self.getInfo()
        print(buddy_info.uri + ':' + buddy_info.bi.presStatus.statusText)