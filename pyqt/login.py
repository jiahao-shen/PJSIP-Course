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
from PyQt5.QtWidgets import QDialog, QLabel, QGridLayout, QLineEdit, QPushButton
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

        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap('image/phone.png'))
        self.grid.addWidget(self.logo_label, 0, 0, 3, 1)

        self.title = QLabel('SIP Account Setup')
        self.title.setFont(FONT_TITLE)
        self.grid.addWidget(self.title, 0, 1, 2, 2)

        self.domain_label = QLabel('Domain')
        self.domain_label.setFont(FONT_CONTENT)
        self.grid.addWidget(self.domain_label, 2, 1)

        self.domain = QLineEdit(DEFAULT_DOMAIN)
        self.domain.setFont(FONT_CONTENT)
        self.domain.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.domain, 2, 2, 1, 2)

        self.username_label = QLabel('Username')
        self.username_label.setFont(FONT_CONTENT)
        self.grid.addWidget(self.username_label, 3, 1)

        self.username = QLineEdit(DEFAULT_USERNAME)
        self.username.setFont(FONT_CONTENT)
        self.username.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.username, 3, 2, 1, 2)

        self.password_label = QLabel('Password')
        self.password_label.setFont(FONT_CONTENT)
        self.grid.addWidget(self.password_label, 4, 1)

        self.password = QLineEdit(DEFAULT_USERNAME)
        self.password.setFont(FONT_CONTENT)
        self.password.setAlignment(Qt.AlignCenter)
        self.password.setEchoMode(QLineEdit.Password)
        self.grid.addWidget(self.password, 4, 2, 1, 2)

        self.login_button = QPushButton('Login')
        # self.login_button.setFont(FONT_CONTENT)
        self.login_button.clicked.connect(self._login)
        self.grid.addWidget(self.login_button, 5, 2)

        self.exit_button = QPushButton('Exit')
        # self.exit_button.setFont(FONT_CONTENT)
        self.exit_button.clicked.connect(self._exit)
        self.grid.addWidget(self.exit_button, 5, 3)

        self.show()

    def _login(self):
        print('login')

    def _exit(self):
        print('exit')