"""
# coding:utf-8
@Time    : 2021/07/17
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : workspace_frame.py
@Desc    : workspace_frame
@Software: PyCharm
"""
from ui.workspace_view import Ui_Form
from PyQt5.QtWidgets import QWidget
from utils.common import read_qss, basedir


class WorkspaceFrame(Ui_Form, QWidget):
    def __init__(self):
        super(WorkspaceFrame, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(read_qss(basedir + '/resources/base.qss'))
        self.workspace_listWidget.setCurrentRow(0)
        self.workspace_stackedWidget.setAutoFillBackground(True)
