import pjsua2 as pj
import time


def test():
    ep = pj.Endpoint()  # Endpoint

    ep_cfg = pj.EpConfig()  # Endpoint Configuration
    # ep_cfg.uaConfig   # User Agent settings
    # ep_cfg.medConfig  # Media global settings
    ep_cfg.logConfig.level = 1  # Logging settings

    # Create and initialize library
    ep.libCreate()
    ep.libInit(ep_cfg)

    # Create SIP transport. Error handling sample is shown
    sipTpConfig = pj.TransportConfig()
    sipTpConfig.port = 5070
    ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, sipTpConfig)

    # Start the library
    ep.libStart()

    acfg = pj.AccountConfig()
    acfg.idUri = "sip:127.0.0.1"
    # acfg.regConfig.registrarUri = "sip:27.102.107.237"
    # cred = pj.AuthCredInfo("digest", "*", "1002",
                        #    pj.PJSIP_CRED_DATA_PLAIN_PASSWD, "1002")
    # acfg.sipConfig.authCreds.append(cred)

    acc = pj.Account()
    acc.create(acfg)

    call = pj.Call(acc)
    prm = pj.CallOpParam(True)
    call.makeCall("sip:127.0.0.1:5060", prm)

    # time.sleep(20)

    # Destroy the library
    ep.libDestroy()


if __name__ == '__main__':
    test()
