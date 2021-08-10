"""
# coding:utf-8
@Time    : 2021/08/10
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : request_set_view.py
@Desc    : request_set_view
@Software: PyCharm
"""
from ui.component.request_set_view import Ui_Form
from PyQt5.QtWidgets import QWidget


class RequestSetView(QWidget, Ui_Form):
    def __init__(self):
        super(RequestSetView, self).__init__()
        self.setupUi(self)
        self.conn_timeout_lineEdit.setProperty('class', 'set-lineedit')
        self.read_timeout_lineEdit.setProperty('class', 'set-lineedit')
        self.ssl_checkBox.clicked.connect(lambda: self.check('ssl'))
        self.redirect_checkBox.clicked.connect(lambda: self.check('redirect'))
        self.ssl_checkBox.setProperty('class', 'set-check')
        self.redirect_checkBox.setProperty('class', 'set-check')
        self.conn_timeout_lineEdit.setText('30')
        self.read_timeout_lineEdit.setText('30')

    def check(self, tag):
        if tag == 'ssl':
            if self.ssl_checkBox.isChecked():
                self.ssl_checkBox.setText('ON')
            else:
                self.ssl_checkBox.setText('OFF')

        if tag == 'redirect':
            if self.redirect_checkBox.isChecked():
                self.redirect_checkBox.setText('ON')
            else:
                self.redirect_checkBox.setText('OFF')
