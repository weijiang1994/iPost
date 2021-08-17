"""
coding:utf-8
file: request_body_view.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/8/14 18:51
@desc:
"""
from PyQt5.QtWidgets import QWidget
from ui.component.request_body_view import Ui_Form


class RequestBody(Ui_Form, QWidget):

    def __init__(self):
        super(RequestBody, self).__init__()
        self.setupUi(self)
