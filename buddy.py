"""
@project: PJSIP-Lab
@author: sam
@file buddy.py
@ide: Visual Studio Code
@time: 2019-11-27 21:36:37
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj 

class Buddy(pj.Buddy):
    def __init__(self, app, iid):
        pj.Buddy.__init__(self)
        self.app = app
        self.iid = iid
        self.cfg = pj.BuddyConfig()

    def onBuddyState(self):
        self.app.update_buddy(self)

    def status(self):
        bi = self.getInfo()
        status = ''
        if bi.subState == pj.PJSIP_EVSUB_STATE_ACCEPTED:
            pass
            # print('PJSIP_EVSUB_STATE_ACCEPTED')
        elif bi.subState == pj.PJSIP_EVSUB_STATE_ACTIVE:
            print(bi.presStatus.status)
            if bi.presStatus.status == pj.PJSUA_BUDDY_STATUS_ONLINE:
                status = bi.presStatus.statusText
                if not status:
                    status = 'Online'
            elif bi.presStatus.status == pj.PJSUA_BUDDY_STATUS_OFFLINE:
                status = 'Offline'
            else:
                status = 'Unknown'
        elif bi.subState == pj.PJSIP_EVSUB_STATE_NULL:
            # print('PJSIP_EVSUB_STATE_NULL')
            status = 'PJSIP_EVSUB_STATE_NULL'
        elif bi.subState == pj.PJSIP_EVSUB_STATE_PENDING:
            # print('PJSIP_EVSUB_STATE_PENDING')
            status = 'PJSIP_EVSUB_STATE_PENDING'
        elif bi.subState == pj.PJSIP_EVSUB_STATE_SENT:
            # print('PJSIP_EVSUB_STATE_SENT')
            status = 'PJSIP_EVSUB_STATE_SENT'
        elif bi.subState == pj.PJSIP_EVSUB_STATE_TERMINATED:
            # print('PJSIP_EVSUB_STATE_TERMINATED')
            status = 'PJSIP_EVSUB_STATE_TERMINATED'
        elif bi.subState == pj.PJSIP_EVSUB_STATE_UNKNOWN:
            # print('PJSIP_EVSUB_STATE_UNKNOWN')
            status = 'PJSIP_EVSUB_STATE_UNKNOWN'
        return status