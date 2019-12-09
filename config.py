"""
@project: PJSIP-Lab
@author: sam
@file config.py
@ide: Visual Studio Code
@time: 2019-11-25 11:36:37
@blog: https://jiahaoplus.com
"""
from enum import Enum

# SIP Configuration
DEFAULT_DOMAIN = '27.102.107.237'


# GUI Configuration
TITLE = ('Arial', 20, 'bold')
CONTENT = ('Arial', 15, 'normal')
MESSGAE = ('Arial', 20, 'normal')

# Color
COLOR_BACKGROUND = '#FDFDFD'
COLOR_SEND_BUBBLE = '#D9F4FE'
COLOR_RECEIVE_BUBBLE = '#F3F3F3'
COLOR_TIME = '#CDCCCC'
# Audio State
class AudioState(Enum):
    CALLING = 'Calling...'
    CONNECT = 'Connect'
    DISCONNECT = 'Disconnect'
    HOLD = 'Holding...'

# Message State
class MessageState(Enum):
    SEND = 'Send'
    RECEIVE = 'Receive'
    INFO = 'Info'
    NULL = 'Null'
