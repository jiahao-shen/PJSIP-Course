import pjsua2 as pj
import time


def test():
    ep = pj.Endpoint()  # Endpoint

    ep_cfg = pj.EpConfig()  # Endpoint Configuration
    # ep_cfg.uaConfig   # User Agent settings
    # ep_cfg.medConfig  # Media global settings
    # ep_cfg.logConfig  # Logging settings

    # Create and initialize library
    ep.libCreate()
    ep.libInit(ep_cfg)

    # Create SIP transport. Error handling sample is shown
    sipTpConfig = pj.TransportConfig()
    sipTpConfig.port = 5060
    ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, sipTpConfig)

    # Start the library
    ep.libStart()

    acfg = pj.AccountConfig()
    acfg.idUri = 'sip:12345@10.105.240.15'
    cred = pj.AuthCredInfo("digest", "*", "565", pj.PJSIP_CRED_DATA_PLAIN_PASSWD, "258667")
    acfg.sipConfig.authCreds.append(cred)
    
    acc = pj.Account()
    acc.create(acfg)
    # time.sleep(10)

    # Destroy the library
    ep.libDestroy()


if __name__ == '__main__':
    test()
