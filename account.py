"""
@project: PJSIP-Lab
@author: sam
@file account.py
@ide: Visual Studio Code
@time: 2019-11-26 10:41:37
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj


class Account(pj.Account):
    def __init__(self, app):
        pj.Account.__init__(self)
        self.app = app

    def onIncomingCall(self, prm):
        print('onIncomingCall')
        super().onIncomingCall(prm)

    def onInstantMessage(self, prm):
        print('onInstantMessgae')
        super().onInstantMessage(prm)

    def onInstantMessageStatus(self, prm):
        print('onInstantMessageStatus')
        super().onInstantMessageStatus(prm)

    def onIncomingSubscribe(self, prm):
        print('onIncomingSubscribe')
        super().onIncomingSubscribe(prm)

    def onRegState(self, prm):
        print('onRegState')
        super().onRegState(prm)

        # print(self.isValid())
        # print(self.getInfo().regLastErr)
        # print(self.getInfo().regIsActive)
        # print(self.getInfo().onlineStatus)
        # print(self.getInfo().onlineStatusText)
        # print(self.getInfo().regIsConfigured)
        # print(self.getInfo().regStatus)
        # print(self.getInfo().regStatusText)

    def onRegStarted(self, prm):
        print('onRegStarted')
        super().onRegStarted(prm)

        # print(self.isValid())
        # print(self.getInfo().regLastErr)
        # print(self.getInfo().regIsActive)
        # print(self.getInfo().onlineStatus)
        # print(self.getInfo().onlineStatusText)
        # print(self.getInfo().regIsConfigured)
        # print(self.getInfo().regStatus)
        # print(self.getInfo().regStatusText)
        # status = '?'
        # if self.isValid():
        #     acc_info = self.getInfo()
        #     if acc_info.regLastErr:
        #         status = self.app.ep.utilStrError(acc_info.regLastErr)
        #     elif acc_info.regIsActive:
        #         if acc_info.onlineStatus:
        #             if len(acc_info.onlineStatusText):
        #                 status = acc_info.onlineStatusText
        #             else:
        #                 status = "Online"
        #         else:
        #             status = "Registered"
        #     else:
        #         if acc_info.regIsConfigured:
        #             if acc_info.regStatus/100 == 2:
        #                 status = "Unregistered"
        #             else:
        #                 status = acc_info.regStatusText
        #         else:
        #             status = "Doesn't register"
        # else:
        #     status = '- not created -'
        # self.

    def onMwiInfo(self, prm):
        print('onMwiInfo')
        super().onMwiInfo(prm)

    def onTypingIndication(self, prm):
        print('onTypingIndication')
        super().onTypingIndication(prm)
