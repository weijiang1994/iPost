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
from utils.common import read_qss
from utils.config import MyConfig
from utils.constants import BASE_CONFIG_PATH, VSS_DARK_THEME_PATH
from controller.api_view import ApiView


class WorkspaceFrame(Ui_Form, QWidget):
    def __init__(self):
        super(WorkspaceFrame, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(read_qss(VSS_DARK_THEME_PATH))
        self.init_ui()
        self.init_slot()
        self.config = MyConfig(path=BASE_CONFIG_PATH)

    def init_ui(self):
        self.workspace_listWidget.setCurrentRow(0)
        self.workspace_stackedWidget.setAutoFillBackground(True)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(0)
        self.tabWidget.setTabsClosable(True)
        self.new_pushButton.setProperty('class', 'SmallBtn')

    def init_slot(self):
        self.new_pushButton.clicked.connect(self.new_request)

    def new_request(self):
        if self.tabWidget.count() >= int(self.config.read_config('base', 'max_tab')):
            QMessageBox.warning(self, '过多的TAB', f'TAB最多不能超过{self.config.read_config("base", "max_tab")},'
                                                f'如需要开启更多请前往设置进行配置!')
            return
        widget = ApiView()
        self.tabWidget.addTab(widget, '新的Request')
        self.tabWidget.setCurrentWidget(widget)
