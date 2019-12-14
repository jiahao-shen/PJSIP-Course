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
            # print('PJSIP_INV_STATE_CALLING')
            self.chat.is_calling()
        elif ci.state == pj.PJSIP_INV_STATE_CONNECTING:
            # print('PJSIP_INV_STATE_CONNECTING')
            pass
        elif ci.state == pj.PJSIP_INV_STATE_DISCONNECTED:
            # print('PJSIP_INV_STATE_DISCONNECTED')
            self.chat.is_disconnect()
        elif ci.state == pj.PJSIP_INV_STATE_CONFIRMED:
            # print('PJSIP_INV_STATE_CONFIRMED')
            self.chat.is_connect()
        elif ci.state == pj.PJSIP_INV_STATE_EARLY:
            # print('PJSIP_INV_STATE_EARLY')
            pass
        elif ci.state == pj.PJSIP_INV_STATE_INCOMING:
            # print('PJSIP_INV_STATE_INCOMING')
            pass
        elif ci.state == pj.PJSIP_INV_STATE_NULL:
            # print('PJSIP_INV_STATE_NULL')
            pass

    def onCallMediaState(self, prm):
        # am = self.getAudioMedia(-1)
        # mgr = Endpoint.instance.audDevManager()
        # am.startTransmit(mgr.getPlaybackDevMedia())
        # mgr.getCaptureDevMedia().startTransmit(am)

        ci = self.getInfo()
        for mi in ci.media:
            if mi.type == pj.PJMEDIA_TYPE_AUDIO:
                am = self.getAudioMedia(mi.index)
                mgr = Endpoint.instance.audDevManager()

                mgr.getCaptureDevMedia().startTransmit(am)
                am.startTransmit(mgr.getPlaybackDevMedia())
            elif mi.type == pj.PJMEDIA_TYPE_VIDEO:
                if mi.videoIncomingWindowId != pj.INVALID_ID:
                    vid_win = pj.VideoWindow(mi.videoIncomingWindowId)
                    vid_pre = pj.VideoPreview(mi.videoCapDev)

                    self.chat.show_video(vid_win, vid_pre)
                else:
                    print('Unkown Error')

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
