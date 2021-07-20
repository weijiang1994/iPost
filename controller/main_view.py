"""
# coding:utf-8
@Time    : 2021/07/17
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : main_view.py
@Desc    : main_view
@Software: PyCharm
"""
from PyQt5.QtWidgets import QMainWindow
from ui.main_window import Ui_MainWindow
from controller.workspace_frame import WorkspaceFrame
from utils.common import read_qss, basedir


class MainView(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.setupUi(self)
        self.label.setVisible(False)
        self.gridLayout.addWidget(WorkspaceFrame())
        self.setStyleSheet(read_qss(basedir + '/resources/vss-dark.qss'))


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = MainView()
    win.setWindowTitle('iPost Version 1.0.14 Beta')
    win.show()
    app.exec_()
