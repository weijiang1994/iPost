"""
coding:utf-8
file: api_view.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/7/18 20:51
@desc:
"""
from PyQt5.QtWidgets import QWidget, QMessageBox
from ui.api_view import Ui_Form
from utils.common import read_qss, basedir, update_btn_stylesheet, BUTTON_NORMAL, BUTTON_SELECTED
import json
import requests
from controller.component.table_view import HeadersTableView, ParamsTableView
from threading import Thread
from PyQt5.QtCore import pyqtSignal
import traceback


class ApiView(Ui_Form, QWidget):
    request_done = pyqtSignal(list)

    def __init__(self):
        super(ApiView, self).__init__()
        self.setupUi(self)
        self.setStyleSheet(read_qss(basedir + '/resources/base.qss'))
        self.init_slot()
        self.buttons = [self.params_pushButton, self.headers_pushButton, self.body_pushButton, self.cookies_pushButton]
        self.init_ui()

    def init_ui(self):
        update_btn_stylesheet(self.buttons, 0)
        self.api_stackedWidget.removeWidget(self.page)
        self.api_stackedWidget.removeWidget(self.page_2)
        self.api_stackedWidget.addWidget(ParamsTableView())
        self.api_stackedWidget.addWidget(HeadersTableView())
        self.api_stackedWidget.addWidget(QWidget())
        self.api_stackedWidget.addWidget(QWidget())
        self.send_pushButton.setProperty('class', 'Postman')
        self.api_url_lineEdit.setProperty('class', 'ApiUrl')

    def init_slot(self):
        self.send_pushButton.clicked.connect(self.send)
        self.params_pushButton.clicked.connect(lambda: self.choose_item('params'))
        self.headers_pushButton.clicked.connect(lambda: self.choose_item('headers'))
        self.body_pushButton.clicked.connect(lambda: self.choose_item('body'))
        self.cookies_pushButton.clicked.connect(lambda: self.choose_item('cookies'))
        self.request_done.connect(self.render_result)

    def render_result(self, list_data):
        self.textBrowser.clear()
        self.textBrowser.insertPlainText(list_data[1])

    def send(self):
        api_url = self.api_url_lineEdit.text()
        if api_url == '' or api_url is None:
            QMessageBox.warning(self, '错误', 'URL地址不能为空!')
            return
        th = Thread(target=self.send_request, args=(api_url,))
        th.setDaemon(True)
        th.start()

    def send_request(self, api_url):
        try:
            res = requests.get(api_url)
            json_text = json.dumps(res.json(), indent=4, ensure_ascii=False, sort_keys=True)
            self.request_done.emit([True, json_text])
        except Exception as e:
            self.request_done.emit([False, f'获取接口数据出错!\n错误信息:\n{str(traceback.format_exc())}\n接口原始数据：\n{res.text}'])

    def choose_item(self, tag):
        if tag == 'params':
            update_btn_stylesheet(self.buttons, index=0)
            self.api_stackedWidget.setCurrentIndex(0)

        elif tag == 'headers':
            update_btn_stylesheet(self.buttons, index=1)
            self.api_stackedWidget.setCurrentIndex(1)

        elif tag == 'body':
            update_btn_stylesheet(self.buttons, index=2)
            self.api_stackedWidget.setCurrentIndex(2)

        else:
            update_btn_stylesheet(self.buttons, index=3)
            self.api_stackedWidget.setCurrentIndex(3)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = ApiView()
    win.show()
    sys.exit(app.exec_())
