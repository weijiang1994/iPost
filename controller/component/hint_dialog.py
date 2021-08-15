"""
coding:utf-8
file: hint_dialog.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/8/15 21:02
@desc:
"""
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.Qt import Qt
from ui.component.hint_base_view import Ui_Form
from utils.constants import LEVELBG, HINT_DIALOG_BASE_ATTR


class HintBase(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(HintBase, self).__init__()
        self.setupUi(self)
        self.setObjectName('hint')
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.center()
        self.oldPos = self.pos()
        self.show()
        self.close_pushButton.clicked.connect(self.close)
        self.setStyleSheet(HINT_DIALOG_BASE_ATTR)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def center(self):
        qr = self.frameGeometry()
        if not self.parent:
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        else:
            try:
                pp = self.parent.geometry().center()
                qr.moveCenter(pp)
                self.move(qr.topLeft())
            except Exception:
                import traceback
                print(traceback.format_exc())


class SuccessHintDialog(HintBase):
    pass


class ErrorHintDialog(HintBase):
    pass


class InfoHintDialog(HintBase):
    pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = HintBase()
    win.show()
    sys.exit(app.exec_())
