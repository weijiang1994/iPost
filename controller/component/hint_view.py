"""
# coding:utf-8
@Time    : 2021/08/10
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : hint_view.py
@Desc    : hint_view
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5 import QtGui, QtCore
from PyQt5.Qt import Qt


class HintWidget(QWidget):
    def __init__(self, msg=None):
        super(HintWidget, self).__init__()
        self.label = None
        self.msg = msg
        self.g_layout = QGridLayout()
        self.init_ui()

    def init_ui(self):
        self.label = QLabel(self.msg if self.msg is not None else 'No Hint Message')
        self.g_layout.addWidget(self.label)
        self.g_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.g_layout)
        self.setGeometry(300, 300, 200, 120)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = HintWidget()
    win.show()
    sys.exit(app.exec_())
