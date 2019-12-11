"""
@project: PJSIP-Lab
@author: sam
@file account.py
@ide: Visual Studio Code
@time: 2019-11-26 10:41:37
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj

from call import Call

class Account(pj.Account):
    def __init__(self, app):
        pj.Account.__init__(self)
        self.app = app
        self.cfg = pj.AccountConfig()
    
    def status(self):
        status = '?'
        if self.isValid():
            ai = self.getInfo()
            if ai.regLastErr:
                status = self.app.ep.utilStrError(ai.regLastErr)
            elif ai.regIsActive:
                if ai.onlineStatus:
                    if len(ai.onlineStatusText):
                        status = ai.onlineStatusText
                    else:
                        status = "Online"
                else:
                    status = "Registered"
            else:
                if ai.regIsConfigured:
                    if ai.regStatus/100 == 2:
                        status = "Unregistered"
                    else:
                        status = ai.regStatusText
                else:
                    status = "Doesn't register"
        else:
            status = '- not created -'
        return status

    def onIncomingCall(self, prm):
        self.app.incoming_call(prm)

    def onInstantMessage(self, prm):
        try:
            print(prm.msgBody)
            self.app.instant_message(prm.fromUri, prm.msgBody)
        except:
            pass

    def onInstantMessageStatus(self, prm):
        print('onInstantMessageStatus')
        super().onInstantMessageStatus(prm)

    def onIncomingSubscribe(self, prm):
        print('onIncomingSubscribe')
        super().onIncomingSubscribe(prm)

    def onRegState(self, prm):
        print('onRegState')
        self.app.update_account()
        

    def onRegStarted(self, prm):
        print('onRegStarted')
        super().onRegStarted(prm)

        
    def onMwiInfo(self, prm):
        print('onMwiInfo')
        super().onMwiInfo(prm)

    def onTypingIndication(self, prm):
        print('onTypingIndication')
        super().onTypingIndication(prm)
