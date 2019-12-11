"""
@project: PJSIP-Lab
@author: sam
@file utils.py
@ide: Visual Studio Code
@time: 2019-11-25 21:27:25
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj

from endpoint import Endpoint


def validateUri(uri):
    return Endpoint.instance.utilVerifyUri(uri) == pj.PJ_SUCCESS


def validateSipUri(uri):
    return Endpoint.instance.utilVerifySipUri(uri) == pj.PJ_SUCCESS


if __name__ == '__main__':
    print(preprocess_message('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'))
