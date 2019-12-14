"""
@project: PJSIP-Lab
@author: sam
@file config.py
@ide: Visual Studio Code
@time: 2019-11-25 11:36:37
@blog: https://jiahaoplus.com
"""
from enum import Enum
from PyQt5.QtGui import QFont

# SIP Configuration
# DEFAULT_DOMAIN = '27.102.107.237'
DEFAULT_DOMAIN = '10.210.63.101'
DEFAULT_USERNAME = '1001'


# GUI Configuration
FONT_TITLE = QFont('Arial', 20, 75)
FONT_CONTENT = QFont('Arial', 15, 50)
FONT_MESSAGE = QFont('Arial', 20, 50)


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
