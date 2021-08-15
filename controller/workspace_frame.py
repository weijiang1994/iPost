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
from PyQt5.QtWidgets import QWidget, QMessageBox, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from utils.common import read_qss
from utils.config import MyConfig
from utils.constants import BASE_CONFIG_PATH, VSS_DARK_THEME_PATH, Icon
from controller.api_view import ApiView
from controller.component.hint_dialog import HintBase


class WorkspaceFrame(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super(WorkspaceFrame, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.init_slot()
        self.config = MyConfig(path=BASE_CONFIG_PATH)
        self.parent = parent
        print(self.parent.geometry())

    def init_ui(self):
        self.workspace_listWidget.setCurrentRow(0)
        self.workspace_stackedWidget.setAutoFillBackground(True)
        self.tabWidget.removeTab(1)
        self.tabWidget.removeTab(0)
        self.tabWidget.setTabsClosable(True)
        self.new_pushButton.setProperty('class', 'SmallBtn')
        self.tabWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tabWidget.customContextMenuRequested.connect(self.tab_menu)
        self.tabWidget.setMovable(True)

    def tab_menu(self, pos):
        if self.tabWidget.count() <= 0:
            return
        menu = QMenu()
        menu.setStyleSheet(read_qss(VSS_DARK_THEME_PATH))
        menu.setProperty('class', 'sub-menu')
        close_cur = QAction('关闭当前选项')
        close_right = QAction('关闭右侧选项')
        close_left = QAction('关闭左侧选项')
        close_other = QAction('关闭其他选项')
        close_all = QAction('关闭所有选项')
        save_cur = QAction('保存当前选项')
        close_cur.setIcon(QIcon(Icon.LOCATION.value))
        close_right.setIcon(QIcon(Icon.ALIGN_RIGHT.value))
        close_left.setIcon(QIcon(Icon.ALIGN_LEFT.value))
        close_all.setIcon(QIcon(Icon.ALIGN_CENTER.value))
        save_cur.setIcon(QIcon(Icon.SAVE.value))

        for action in [close_cur, close_right, close_left, close_other, close_all, save_cur]:
            menu.addAction(action)
        action = menu.exec_(self.tabWidget.mapToGlobal(pos))
        if action == close_cur:
            self.tabWidget.removeTab(self.tabWidget.currentIndex())

        elif action == close_right:
            cur_idx = self.tabWidget.currentIndex()
            for i in range(cur_idx, self.tabWidget.count()):
                self.tabWidget.removeTab(cur_idx+1)

        elif action == close_left:
            cur_idx = self.tabWidget.currentIndex()
            for i in range(cur_idx):
                self.tabWidget.removeTab(0)

        elif action == close_other:
            cur_idx = self.tabWidget.currentIndex()
            for i in range(cur_idx):
                self.tabWidget.removeTab(0)
            cur_idx = self.tabWidget.currentIndex()
            counts = self.tabWidget.count()
            for i in range(cur_idx, counts):
                self.tabWidget.removeTab(cur_idx + 1)

        elif action == close_all:
            counts = self.tabWidget.count()
            print(counts)
            for i in range(counts):
                self.tabWidget.removeTab(0)

    def init_slot(self):
        self.new_pushButton.clicked.connect(self.new_request)
        self.tabWidget.tabCloseRequested.connect(self.tab_close)

    def tab_close(self, idx):
        self.tabWidget.removeTab(idx)

    def new_request(self):
        if self.tabWidget.count() >= int(self.config.read_config('base', 'max_tab')):
            self.hb = HintBase(parent=self.parent)
            # QMessageBox.warning(self, '过多的TAB', f'TAB最多不能超过{self.config.read_config("base", "max_tab")},'
            #                                     f'如需要开启更多请前往设置进行配置!')
            return
        #
        widget = ApiView()
        self.tabWidget.addTab(widget, '新的Request')
        self.tabWidget.setCurrentWidget(widget)
