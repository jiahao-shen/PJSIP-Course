"""
@project: PJSIP-Lab
@author: sam
@file login.py
@ide: Visual Studio Code
@time: 2019-11-25 12:36:37
@blog: https://jiahaoplus.com
"""
import pjsua2 as pj


from utils import *
from config import *
from endpoint import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap


class LoginDialog(QDialog):

    def __init__(self, parent, cfg):
        super().__init__(parent, Qt.WindowStaysOnTopHint)
        self.parent = parent
        self.cfg = cfg
        self.ok = False

        """
        Initialize UI
        """
        self.setWindowTitle('Login')

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.logo_label = QLabel(self)
        self.logo_label.setPixmap(QPixmap('image/phone.png'))
        self.grid.addWidget(self.logo_label, 0, 0, 3, 1)

        self.title = QLabel('fuck', self)
        self.title.setFont(FONT_TITLE)

        self.show()
