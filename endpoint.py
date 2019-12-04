"""
@project: PJSIP-Lab
@author: sam
@file endpoint.py
@ide: Visual Studio Code
@time: 2019-12-03 17:42:37
@blog: https://jiahaoplus.com
"""

import pjsua2 as pj


class Endpoint(pj.Endpoint):
    """
    This is high level Python object inherited from pj.Endpoint
    """
    instance = None

    def __init__(self):
        pj.Endpoint.__init__(self)
        Endpoint.instance = self


def validateUri(uri):
    return Endpoint.instance.utilVerifyUri(uri) == pj.PJ_SUCCESS


def validateSipUri(uri):
    return Endpoint.instance.utilVerifySipUri(uri) == pj.PJ_SUCCESS
