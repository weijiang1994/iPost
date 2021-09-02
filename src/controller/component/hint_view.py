"""
# coding:utf-8
@Time    : 2021/08/10
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : hint_view.py
@Desc    : hint_view
@Software: PyCharm
"""
from src.ui.component.hint_view import Ui_Form
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout
from PyQt5 import QtGui


class HintWidget(QWidget, Ui_Form):
    def __init__(self, msg=None, pix=None, detail=None):
        super(HintWidget, self).__init__()
        self.setupUi(self)
        self.pix = pix
        self.detail = detail
        self.msg = msg
        self.g_layout = QGridLayout()
        self.v_layout = QVBoxLayout()
        self.init_ui()

    def init_ui(self):
        if self.pix is not None:
            self.icon_label.setPixmap(QtGui.QPixmap(self.pix))
        else:
            self.icon_label.setVisible(False)
        self.hint_msg_label.setText(self.msg if self.msg is not None else 'No Hint Message')
        if self.detail is not None:
            self.detail_label.setText(self.detail)
            self.detail_label.setProperty('class', 'detail-label')
        else:
            self.detail_label.setVisible(False)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = HintWidget()
    win.show()
    sys.exit(app.exec_())
