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
from PyQt5.QtWidgets import QWidget, QMessageBox
from utils.common import read_qss, basedir
from controller.api_view import ApiView


class WorkspaceFrame(Ui_Form, QWidget):
    def __init__(self):
        super(WorkspaceFrame, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(read_qss(basedir + '/resources/base.qss'))
        self.init_ui()
        self.init_slot()

    def init_ui(self):
        self.workspace_listWidget.setCurrentRow(0)
        self.workspace_stackedWidget.setAutoFillBackground(True)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(0)
        self.tabWidget.setTabsClosable(True)

    def init_slot(self):
        self.new_pushButton.clicked.connect(self.new_request)

    def new_request(self):
        if self.tabWidget.count() > 2:
            return
        widget = ApiView()
        self.tabWidget.addTab(widget, 'Test Request')
        self.tabWidget.setCurrentWidget(widget)
