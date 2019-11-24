{ 
   "EpConfig":             { 
      "UaConfig":             { 
         "maxCalls":             4,
         "threadCnt":            0,
         "mainThreadOnly":       true,
         "nameserver":           [ ],
         "userAgent":            "pygui-2.9",
         "stunServer":           [ ],
         "stunTryIpv6":          false,
         "stunIgnoreFailure":    true,
         "natTypeInSdp":         1,
         "mwiUnsolicitedEnabled": true
      },
      "LogConfig":            { 
         "msgLogging":           1,
         "level":                5,
         "consoleLevel":         5,
         "decor":                25328,
         "filename":             "pygui.log",
         "fileFlags":            4360
      },
      "MediaConfig":          { 
         "clockRate":            16000,
         "sndClockRate":         0,
         "channelCount":         1,
         "audioFramePtime":      20,
         "maxMediaPorts":        254,
         "hasIoqueue":           true,
         "threadCnt":            1,
         "quality":              8,
         "ptime":                0,
         "noVad":                false,
         "ilbcMode":             30,
         "txDropPct":            0,
         "rxDropPct":            0,
         "ecOptions":            0,
         "ecTailLen":            200,
         "sndRecLatency":        100,
         "sndPlayLatency":       140,
         "jbInit":               -1,
         "jbMinPre":             -1,
         "jbMaxPre":             -1,
         "jbMax":                -1,
         "sndAutoCloseTime":     1,
         "vidPreviewEnableNative": true
      }
   },
   "transports":           [ 
      { 
         "type":                 1,
         "enabled":              true,
         "TransportConfig":      { 
            "port":                 0,
            "portRange":            0,
            "publicAddress":        "",
            "boundAddress":         "",
            "qosType":              0,
            "qosParams":            { 
               "qos.flags":            0,
               "qos.dscp_val":         0,
               "qos.so_prio":          0,
               "qos.wmm_prio":         0
            },
            "TlsConfig":            { 
               "CaListFile":           "",
               "certFile":             "",
               "privKeyFile":          "",
               "password":             "",
               "CaBuf":                "",
               "certBuf":              "",
               "privKeyBuf":           "",
               "method":               0,
               "ciphers":              [ ],
               "verifyServer":         false,
               "verifyClient":         false,
               "requireClientCert":    false,
               "msecTimeout":          0,
               "qosType":              0,
               "qosParams":            { 
                  "qos.flags":            0,
                  "qos.dscp_val":         0,
                  "qos.so_prio":          0,
                  "qos.wmm_prio":         0
               },
               "qosIgnoreError":       true
            }
         }
      },
      { 
         "type":                 2,
         "enabled":              true,
         "TransportConfig":      { 
            "port":                 0,
            "portRange":            0,
            "publicAddress":        "",
            "boundAddress":         "",
            "qosType":              0,
            "qosParams":            { 
               "qos.flags":            0,
               "qos.dscp_val":         0,
               "qos.so_prio":          0,
               "qos.wmm_prio":         0
            },
            "TlsConfig":            { 
               "CaListFile":           "",
               "certFile":             "",
               "privKeyFile":          "",
               "password":             "",
               "CaBuf":                "",
               "certBuf":              "",
               "privKeyBuf":           "",
               "method":               0,
               "ciphers":              [ ],
               "verifyServer":         false,
               "verifyClient":         false,
               "requireClientCert":    false,
               "msecTimeout":          0,
               "qosType":              0,
               "qosParams":            { 
                  "qos.flags":            0,
                  "qos.dscp_val":         0,
                  "qos.so_prio":          0,
                  "qos.wmm_prio":         0
               },
               "qosIgnoreError":       true
            }
         }
      },
      { 
         "type":                 3,
         "enabled":              false,
         "TransportConfig":      { 
            "port":                 0,
            "portRange":            0,
            "publicAddress":        "",
            "boundAddress":         "",
            "qosType":              0,
            "qosParams":            { 
               "qos.flags":            0,
               "qos.dscp_val":         0,
               "qos.so_prio":          0,
               "qos.wmm_prio":         0
            },
            "TlsConfig":            { 
               "CaListFile":           "",
               "certFile":             "",
               "privKeyFile":          "",
               "password":             "",
               "CaBuf":                "",
               "certBuf":              "",
               "privKeyBuf":           "",
               "method":               0,
               "ciphers":              [ ],
               "verifyServer":         false,
               "verifyClient":         false,
               "requireClientCert":    false,
               "msecTimeout":          0,
               "qosType":              0,
               "qosParams":            { 
                  "qos.flags":            0,
                  "qos.dscp_val":         0,
                  "qos.so_prio":          0,
                  "qos.wmm_prio":         0
               },
               "qosIgnoreError":       true
            }
         }
      }
   ],
   "accounts":             [ ]
}