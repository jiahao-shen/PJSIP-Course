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
        print(ci.state)

    def onCallMediaState(self, prm):
        self.am = self.getAudioMedia(-1)
        self.mgr = Endpoint.instance.audDevManager()
        self.am.startTransmit(self.mgr.getPlaybackDevMedia())
        self.mgr.getCaptureDevMedia().startTransmit(self.am)
        
        # ci = self.getInfo()
        # for mi in ci.media:
        #     if mi.type == pj.PJMEDIA_TYPE_AUDIO:
        #         am = pj.AudioMedia.typecastFromMedia(self.getMedia(mi.index))
        #         # Connect the call audio media to sound device
        #         mgr = Endpoint.instance.audDevManager()
        #         am.startTransmit(mgr.getPlaybackDevMedia())
        #         mgr.getCaptureDevMedia().startTransmit(am)

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


