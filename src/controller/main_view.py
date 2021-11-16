"""
# coding:utf-8
@Time    : 2021/07/17
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : main_view.py
@Desc    : main_view
@Software: PyCharm
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from src.ui.main_window import Ui_MainWindow
from src.controller.workspace_frame import WorkspaceFrame
from src.utils.common import read_qss
from src.utils.constants import basedir
from src.utils.constants import VSS_DARK_THEME_PATH


class MainView(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)
        self.label.setVisible(False)
        self.gridLayout.addWidget(WorkspaceFrame(parent=self))
        self.menu.setProperty('class', 'main-menu')
        self.menu_2.setProperty('class', 'main-menu')
        self.menu_3.setProperty('class', 'main-menu')
        self.menu_4.setProperty('class', 'main-menu')


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = MainView()
    win.setMinimumWidth(1287)
    win.setWindowIcon(QIcon(basedir + '/resources/images/logo.png'))
    win.setStyleSheet(read_qss(VSS_DARK_THEME_PATH))
    win.setWindowTitle('iPost Version 1.0.14 Beta')
    win.show()
    app.exec_()
