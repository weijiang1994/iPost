"""
coding:utf-8
file: api_view.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/7/18 20:51
@desc:
"""
from PyQt5.QtWidgets import QWidget, QMessageBox, QLabel
from PyQt5.QtGui import QCursor, QMouseEvent
from ui.api_view import Ui_Form
from utils.common import read_qss, basedir, update_btn_stylesheet, BUTTON_NORMAL, BUTTON_SELECTED, display_level, \
    get_cookies_data
from utils.constants import HTTP_CODE_COLOR
import json
import requests
from controller.component.table_view import HeadersTableView, ParamsTableView, ResponseTable
from controller.component.json_editor import JSONEditor
from threading import Thread
from PyQt5.QtCore import pyqtSignal, QEvent, QPropertyAnimation
import traceback


class ApiView(Ui_Form, QWidget):
    request_done = pyqtSignal(list)

    def __init__(self):
        super(ApiView, self).__init__()
        self.setupUi(self)
        self.params_tw = ParamsTableView()
        self.headers_tw = HeadersTableView()
        self.editor = JSONEditor()
        self.x_position = 0
        self.y_position = 0
        self.init_slot()
        self.buttons = [self.params_pushButton, self.headers_pushButton, self.body_pushButton, self.cookies_pushButton]
        self.res_buttons = [self.res_body_pushButton, self.res_cookies_pushButton, self.res_headers_pushButton]
        self.init_ui()

    def init_ui(self):
        update_btn_stylesheet(self.buttons, 0)
        update_btn_stylesheet(self.res_buttons, 0)
        self.api_stackedWidget.removeWidget(self.page)
        self.api_stackedWidget.removeWidget(self.page_2)
        self.res_stackedWidget.removeWidget(self.page_3)
        self.res_stackedWidget.removeWidget(self.page_4)
        self.api_stackedWidget.addWidget(self.params_tw)
        self.api_stackedWidget.addWidget(self.headers_tw)
        self.api_stackedWidget.addWidget(QWidget())
        self.api_stackedWidget.addWidget(QWidget())
        self.send_pushButton.setProperty('class', 'Postman')
        self.api_url_lineEdit.setProperty('class', 'ApiUrl')
        self.res_stackedWidget.addWidget(self.editor)
        self.api_url_lineEdit.setText('https://2dogz.cn/api/get-soul?counts=10')

    def init_slot(self):
        self.send_pushButton.clicked.connect(self.send)
        self.params_pushButton.clicked.connect(lambda: self.choose_item('params'))
        self.headers_pushButton.clicked.connect(lambda: self.choose_item('headers'))
        self.body_pushButton.clicked.connect(lambda: self.choose_item('body'))
        self.cookies_pushButton.clicked.connect(lambda: self.choose_item('cookies'))
        self.res_body_pushButton.clicked.connect(lambda: self.choose_item('r_body'))
        self.res_headers_pushButton.clicked.connect(lambda: self.choose_item('r_headers'))
        self.res_cookies_pushButton.clicked.connect(lambda: self.choose_item('r_cookies'))
        self.request_done.connect(self.render_result)

    def render_result(self, list_data):
        self.editor.clear()
        self.editor.setText(list_data[1])
        self.send_pushButton.setText('Send')
        self.send_pushButton.setEnabled(True)
        if list_data[0]:
            self.code_label.setText(str(list_data[2]))
            self.code_label.setStyleSheet(f"color:{HTTP_CODE_COLOR.get(list_data[2])}")
            self.time_label.setText(display_level(list_data[3].microseconds, 1000, labels=['us', 'ms', 's'], level=3))
            self.time_label.setStyleSheet(f"color: {HTTP_CODE_COLOR.get(200)}")
            body_size = display_level(int(list_data[4].get('Content-Length', 0)), 1024, labels=['b', 'kb', 'm'],
                                      level=3)
            header_size = display_level(len(str(list_data[4])), 1024, labels=['b', 'kb', 'm'], level=3)
            size = int(list_data[4].get('Content-Length', 0)) + len(str(list_data[4]))
            size = display_level(size, 1024, labels=['b', 'kb', 'm'], level=3)
            self.size_label.setText(size)
            self.size_label.setStyleSheet(f'color: {HTTP_CODE_COLOR.get(200)}')
            self.size_label.setToolTip(f'<p>Response Size: {size}</p>'
                                       f'<p style="color: white;">Body Size: {body_size}</p>'
                                       f'<p style="color: white;">Header Size: {header_size}</p>')
            if not list_data[5]:
                label = QLabel('请求中暂未包含有cookies')
                self.res_stackedWidget.addWidget(label)
            else:
                cookie_table = ResponseTable(headers=['Name', 'Value', 'Domain', 'Path', 'Expires', 'HttpOnly', 'Secure'])
                cookie_table.render_cookies(get_cookies_data(list_data[5]))
                self.res_stackedWidget.addWidget(cookie_table)

            if list_data[4]:
                headers_table = ResponseTable()
                headers_table.render_data(list_data[4])
                self.res_stackedWidget.addWidget(headers_table)
        else:
            self.code_label.setText(str(list_data[-1]))
            self.code_label.setStyleSheet(f"color:{HTTP_CODE_COLOR.get(list_data[2])}")
            self.time_label.setText('NaN')
            self.size_label.setText('NaN')

    def send(self):
        api_url = self.api_url_lineEdit.text()
        if api_url == '' or api_url is None:
            QMessageBox.warning(self, '错误', 'URL地址不能为空!')
            return
        header_data = {}
        method = self.comboBox.currentText()
        for row in range(self.headers_tw.tableWidget.rowCount()):
            if row not in self.headers_tw.unselect_row:
                header_data[self.headers_tw.tableWidget.cellWidget(row, 0).text()] = \
                    self.headers_tw.tableWidget.item(row, 1).text()
        self.send_pushButton.setText('Sending')
        self.send_pushButton.setEnabled(False)
        th = Thread(target=self.send_request, args=(api_url, method, header_data))
        th.setDaemon(True)
        th.start()

    def send_request(self, api_url, method='GET', headers=None):
        try:
            res = None
            if method == 'GET':
                res = requests.get(api_url, headers=headers if headers else {})
            if method == 'POST':
                res = requests.post(api_url, headers=headers if headers else {})
            if method == 'PUT':
                res = requests.post(api_url, headers=headers if headers else {})
            if method == 'DELETE':
                res = requests.delete(api_url, headers=headers if headers else {})
            json_text = json.dumps(res.json(), indent=4, ensure_ascii=False, sort_keys=True)
            self.request_done.emit([True, json_text, res.status_code, res.elapsed, res.headers, res.cookies])
        except Exception as e:
            if res is not None:
                self.request_done.emit([False, f'获取接口数据出错!\n错误信息:\n{str(traceback.format_exc())}\n接口原始数据：\n'
                                               f'{res.text}', res.status_code])
            else:
                self.request_done.emit([False, f'获取接口数据出错!\n错误信息:\n{str(traceback.format_exc())}'])

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

        elif tag == 'cookies':
            update_btn_stylesheet(self.buttons, index=3)
            self.api_stackedWidget.setCurrentIndex(3)

        elif tag == 'r_body':
            update_btn_stylesheet(self.res_buttons, index=0)
            self.res_stackedWidget.setCurrentIndex(0)

        elif tag == 'r_headers':
            update_btn_stylesheet(self.res_buttons, index=2)
            self.res_stackedWidget.setCurrentIndex(2)

        elif tag == 'r_cookies':
            update_btn_stylesheet(self.res_buttons, index=1)
            self.res_stackedWidget.setCurrentIndex(1)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = ApiView()
    win.show()
    sys.exit(app.exec_())
