"""
@project: PJSIP-Lab
@author: sam
@file main.py
@ide: Visual Studio Code
@time: 2019-11-24 21:36:37
@blog: https://jiahaoplus.com
"""
import sys
import pjsua2 as pj

from config import *
from endpoint import Endpoint
from login import LoginDialog
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QGridLayout, QLineEdit, QPushButton, QTableWidgetItem


class Main(QWidget):

    def __init__(self):
        super().__init__()

        """
        Initialize PJSUA2
        """
        # self.ep = Endpoint()
        # self.ep.libCreate()

        # self.ep_cfg = pj.EpConfig()
        # # self.ep_cfg.uaConfig.threadCnt = 0
        # # self.ep_cfg.uaConfig.mainThreadOnly = True
        # self.ep_cfg.logConfig.level = 0

        # self.ep.libInit(self.ep_cfg)

        # self.sip_cfg = pj.TransportConfig()
        # self.ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, self.sip_cfg)
        # self.ep.libStart()

        # """
        # Initialize Account
        # """
        self.acc = None
        self.domain = DEFAULT_DOMAIN

        self.buddy_list = {}
        self.chat_list = {}

        """
        Initialize UI
        """
        self.setWindowTitle('SIP Client')
        self.setGeometry(300, 300, 300, 300)

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        self.buddy = QLineEdit()
        self.buddy.returnPressed.connect(self._add_buddy)
        self.grid.addWidget(self.buddy, 0, 0, 1, 3)

        self.bud_table = QTableWidget()
        self.bud_table.setColumnCount(2)
        self.bud_table.verticalHeader().setVisible(False)
        self.bud_table.setHorizontalHeaderLabels(['Buddies', 'Status'])
        self.bud_table.setColumnWidth(0, 100)
        self.bud_table.setColumnWidth(1, 160)
        self.grid.addWidget(self.bud_table, 1, 0, 1, 3)

        self.logout_button = QPushButton('Logout')
        self.logout_button.clicked.connect(self._login)
        self.grid.addWidget(self.logout_button, 2, 0)

        self.exit_button = QPushButton('Exit')
        self.exit_button.clicked.connect(self._exit)
        self.grid.addWidget(self.exit_button, 2, 2)
        
        self.show()

        self._login()

    def _add_buddy(self):
        self.bud_table.insertRow(self.bud_table.rowCount())
        self.bud_table.setItem(self.bud_table.rowCount() - 1, 0, QTableWidgetItem(self.buddy.text()))

        self.buddy.setText('')

    def _delete_buddy(self):
        pass

    def update_buddy(self, bud):
        pass

    def update_account(self):
        pass

    def incoming_call(self, prm):
        pass

    def instant_message(self, uri, msg):
        pass

    def _create_chat(self, event):
        pass

    def delete_chat(self, iid):
        pass

    def _login(self):
        # Initialize configuration of account
        acc_cfg = pj.AccountConfig()
        # Create LoginDialog
        dlg = LoginDialog(self, acc_cfg)
        # Wait for response

    def _exit(self):
        # self.ep.libDestroy()
        # self.ep = None
        # self.close()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)

    root = Main()

    sys.exit(app.exec_())
