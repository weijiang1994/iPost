"""
coding:utf-8
file: request_body_view.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/8/14 18:51
@desc:
"""
from PyQt5.QtWidgets import QWidget
from ui.component.request_body_view import Ui_Form
from controller.component.message import Message
from controller.component.hint_view import HintWidget


class RequestBody(Ui_Form, QWidget):

    def __init__(self):
        super(RequestBody, self).__init__()
        self.setupUi(self)
        self.init_ui()
        self.init_slot()

    def init_slot(self):
        self.none_radioButton.clicked.connect(lambda: self.change_page(0))
        self.form_radioButton.clicked.connect(lambda: self.change_page(1))
        self.raw_radioButton.clicked.connect(lambda: self.change_page(2))
        self.binary_radioButton.clicked.connect(lambda: self.change_page(3))

    def change_page(self, idx):
        self.body_stackedWidget.setCurrentIndex(idx)

    def init_ui(self):
        self.body_stackedWidget.removeWidget(self.page)
        self.body_stackedWidget.removeWidget(self.page_2)
        m1 = Message()
        self.body_stackedWidget.addWidget(HintWidget(msg='This request does not have a body.'))
        self.body_stackedWidget.addWidget(m1)
        self.body_stackedWidget.addWidget(m1)
        self.body_stackedWidget.addWidget(m1)
        self.none_radioButton.setChecked(True)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = RequestBody()
    win.show()
    sys.exit(app.exec_())
