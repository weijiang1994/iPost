"""
coding:utf-8
file: api_view.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/7/18 20:51
@desc:
"""
from PyQt5.QtWidgets import QWidget
from ui.api_view import Ui_Form
from utils.common import read_qss, basedir
import requests


class ApiView(Ui_Form, QWidget):

    def __init__(self):
        super(ApiView, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(read_qss(basedir + '/resources/base.qss'))
        self.init_slot()

    def init_slot(self):
        self.send_pushButton.clicked.connect(self.send)

    def send(self):
        api_url = self.api_url_lineEdit.text()
        if api_url == '' or api_url is None:
            return
        res = requests.get(api_url)
        self.textBrowser.setText(res.text)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = ApiView()
    win.show()
    sys.exit(app.exec_())
