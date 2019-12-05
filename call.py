"""
@project: PJSIP-Lab
@author: sam
@file call.py
@ide: Visual Studio Code
@time: 2019-12-04 16:25:00
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj
from endpoint import Endpoint


class Call(pj.Call):

    def __init__(self, acc, uri='', chat=None, call_id=pj.PJSUA_INVALID_ID):
        pj.Call.__init__(self, acc, call_id)
        self.acc = acc
        self.uri = uri
        self.chat = chat

    def onCallState(self, prm):
        ci = self.getInfo()
        if ci.state == pj.PJSIP_INV_STATE_CALLING:
            self.chat.is_calling()
        elif ci.state == pj.PJSIP_INV_STATE_CONFIRMED:
            self.chat.is_connect()
        elif ci.state == pj.PJSIP_INV_STATE_DISCONNECTED:
            self.chat.is_disconnect()

    def onCallMediaState(self, prm):
        am = self.getAudioMedia(-1)
        mgr = Endpoint.instance.audDevManager()
        am.startTransmit(mgr.getPlaybackDevMedia())
        mgr.getCaptureDevMedia().startTransmit(am)
        
    def onInstantMessage(self, prm):
        return super().onInstantMessage(prm)

    def onInstantMessageStatus(self, prm):
        return super().onInstantMessageStatus(prm)

    def onTypingIndication(self, prm):
        return super().onTypingIndication(prm)

    def onDtmfDigit(self, prm):
        return super().onDtmfDigit(prm)

    def onCallMediaTransportState(self, prm):
        return super().onCallMediaTransportState(prm)


