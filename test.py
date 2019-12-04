import time
import pjsua2 as pj
from call import Call


def test_call():
    ep = pj.Endpoint()
    ep.libCreate()

    ep_cfg = pj.EpConfig()
    # ep_cfg.uaConfig.threadCnt = 0
    # ep_cfg.uaConfig.mainThreadOnly = True
    ep_cfg.logConfig.level = 1

    ep.libInit(ep_cfg)

    sip_cfg = pj.TransportConfig()
    ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, sip_cfg)
    ep.libStart()

    print('Account Create')
    acc = pj.Account()
    acc_cfg = pj.AccountConfig()
    acc_cfg.idUri = 'sip:1001@27.102.107.237'
    acc_cfg.regConfig.registrarUri = 'sip:27.102.107.237'
    acc_cfg.regConfig.registerOnAdd = True
    acc_cfg.sipConfig.authCreds.append(pj.AuthCredInfo(
        'digest', '*', '1001', pj.PJSIP_CRED_DATA_PLAIN_PASSWD, '1001'))

    acc.create(acc_cfg)

    print('Call Start')
    call = Call(acc, 'sip:1002@27.102.107.237')
    call_prm = pj.CallOpParam()
    call.makeCall('sip:1002@27.102.107.237', call_prm)

    print('Sleep')
    time.sleep(10)

    ep.libDestroy()
    ep = None


if __name__ == '__main__':
    test_call()