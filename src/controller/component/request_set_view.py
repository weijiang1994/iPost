"""
# coding:utf-8
@Time    : 2021/08/10
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : request_set_view.py
@Desc    : request_set_view
@Software: PyCharm
"""
from src.ui.component.request_set_view import Ui_Form
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIntValidator


class RequestSetView(QWidget, Ui_Form):
    def __init__(self):
        super(RequestSetView, self).__init__()
        self.setupUi(self)
        self.ssl = True
        self.redirect = True
        self.conn_to = 30
        self.read_to = 30
        self.max_redir = 5
        self.init_ui()
        self.init_slot()

    def init_ui(self):
        self.conn_timeout_lineEdit.setProperty('class', 'set-lineedit')
        self.read_timeout_lineEdit.setProperty('class', 'set-lineedit')
        self.max_redirect_lineEdit.setProperty('class', 'set-lineedit')
        self.ssl_checkBox.setProperty('class', 'set-check')
        self.redirect_checkBox.setProperty('class', 'set-check')
        self.conn_timeout_lineEdit.setText(str(self.conn_to))
        self.read_timeout_lineEdit.setText(str(self.read_to))
        self.max_redirect_lineEdit.setText(str(self.max_redir))
        self.conn_timeout_lineEdit.setValidator(QIntValidator(0, 99))
        self.read_timeout_lineEdit.setValidator(QIntValidator(0, 99))
        self.max_redirect_lineEdit.setValidator(QIntValidator(1, 20))
        self.conn_timeout_lineEdit.setPlaceholderText('0~99')
        self.read_timeout_lineEdit.setPlaceholderText('0~99')
        self.max_redirect_lineEdit.setPlaceholderText('0~20')

    def init_slot(self):
        self.ssl_checkBox.clicked.connect(lambda: self.check('ssl'))
        self.redirect_checkBox.clicked.connect(lambda: self.check('redirect'))

    def check(self, tag):
        # 使用点击信号来判断是否被选中了
        if tag == 'ssl':
            if self.ssl_checkBox.isChecked():
                self.ssl_checkBox.setText('ON')
                self.ssl = True
            else:
                self.ssl_checkBox.setText('OFF')
                self.ssl = False

        if tag == 'redirect':
            if self.redirect_checkBox.isChecked():
                self.redirect_checkBox.setText('ON')
                self.redirect = True
            else:
                self.redirect_checkBox.setText('OFF')
                self.redirect = False
