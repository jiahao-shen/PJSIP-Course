"""
@project: PJSIP-Lab
@author: sam
@file utils.py
@ide: PyCharm
@time: 2019-11-25 21:27:25
@blog: https://jiahaoplus.com
"""
from pjsua2 import Endpoint


def validate_sip_uri(uri):
    return Endpoint.utilVerifySipUri(uri)

