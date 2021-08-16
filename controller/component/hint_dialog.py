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
from utils.constants import HINTBG, HINT_DIALOG_BASE_ATTR, Icon
from PyQt5.QtGui import QPixmap


class HintBase(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(HintBase, self).__init__()
        self.setupUi(self)
        self.parent = parent
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.center()
        self.oldPos = self.pos()
        self.show()
        self.close_pushButton.clicked.connect(self.close)
        self.setStyleSheet(HINT_DIALOG_BASE_ATTR)
        self.hint_icon_label.setMaximumSize(40, 40)
        self.hint_icon_label.setScaledContents(True)
        self.hint_icon_label.setMargin(8)

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
            pp = self.parent.geometry().center()
            qr.moveCenter(pp)
            self.move(qr.topLeft())


class SuccessHintDialog(HintBase):
    def __init__(self, msg=''):
        super(SuccessHintDialog, self).__init__()
        self.setStyleSheet(HINT_DIALOG_BASE_ATTR % (HINTBG.get('success'), HINTBG.get('success')))
        self.hint_icon_label.setPixmap(QPixmap(Icon.SUC_ICON.value))
        self.hint_cate_label.setText('成功')
        self.hint_msg_label.setText(msg)


class ErrorHintDialog(HintBase):
    def __init__(self, msg):
        super(ErrorHintDialog, self).__init__()
        self.setStyleSheet(HINT_DIALOG_BASE_ATTR % (HINTBG.get('error'), HINTBG.get('error')))
        self.hint_icon_label.setPixmap(QPixmap(Icon.ERR_ICON.value))
        self.hint_cate_label.setText('错误')
        self.hint_msg_label.setText(msg)


class InfoHintDialog(HintBase):
    def __init__(self, msg):
        super(InfoHintDialog, self).__init__()
        self.setStyleSheet(HINT_DIALOG_BASE_ATTR % (HINTBG.get('info'), HINTBG.get('info')))
        self.hint_icon_label.setPixmap(QPixmap(Icon.INFO_ICON.value))
        self.hint_cate_label.setText('提示')
        self.hint_msg_label.setText(msg)


class WarningHintDialog(HintBase):
    def __init__(self, msg):
        super(WarningHintDialog, self).__init__()
        self.setStyleSheet(HINT_DIALOG_BASE_ATTR % (HINTBG.get('warning'), HINTBG.get('warning')))
        self.hint_icon_label.setPixmap(QPixmap(Icon.INFO_ICON.value))
        self.hint_cate_label.setText('警告')
        self.hint_msg_label.setText(msg)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = SuccessHintDialog('操作成功')
    win.show()
    sys.exit(app.exec_())
