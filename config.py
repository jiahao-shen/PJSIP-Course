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
# DEFAULT_DOMAIN = '27.102.107.237'
DEFAULT_DOMAIN = '10.210.63.101'
DEFAULT_USERNAME = '1001'


# GUI Configuration
FONT_TITLE = ('Arial', 20, 'bold')
FONT_CONTENT = ('Arial', 15, 'normal')
FONT_MESSAGE = ('Arial', 20, 'normal')


# Color
COLOR_BACKGROUND = '#FDFDFD'
COLOR_SEND_BUBBLE = '#D9F4FE'
COLOR_RECEIVE_BUBBLE = '#F3F3F3'
COLOR_TIME = '#CDCCCC'


class AudioState(Enum):
    # Audio State
    CALLING = 'Calling...'
    CONNECT = 'Connect'
    DISCONNECT = 'Disconnect'
    HOLD = 'Holding...'


class MessageState(Enum):
    # Message State
    SEND = 'Send'
    RECEIVE = 'Receive'
    INFO = 'Info'
    NULL = 'Null'
