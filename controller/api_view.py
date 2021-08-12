"""
coding:utf-8
file: api_view.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/7/18 20:51
@desc:
"""
from PyQt5.QtWidgets import QWidget, QMessageBox, QLabel
from PyQt5.Qt import Qt
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QCursor, QMouseEvent
from ui.api_view import Ui_Form
from utils.common import read_qss, basedir, update_btn_stylesheet, BUTTON_NORMAL, BUTTON_SELECTED, display_level, \
    get_cookies_data
from utils.constants import HTTP_CODE_COLOR, Icon
import json
import requests
from controller.component.table_view import HeadersTableView, ParamsTableView, ResponseTable
from controller.component.qsci_editor import JSONEditor, HTMLEditor
from controller.component.hint_view import HintWidget
from controller.component.request_set_view import RequestSetView
from threading import Thread
from PyQt5.QtCore import pyqtSignal, QEvent, QPropertyAnimation
import traceback
from utils.request import RequestSession


class ApiView(Ui_Form, QWidget):
    request_done = pyqtSignal(list)

    def __init__(self):
        super(ApiView, self).__init__()
        self.setupUi(self)
        self.params_tw = ParamsTableView()
        self.headers_tw = HeadersTableView()
        self.editor = JSONEditor()
        self.request_set_view = RequestSetView()
        self.x_position = 0
        self.y_position = 0
        self.init_slot()
        self.buttons = [self.params_pushButton, self.headers_pushButton, self.body_pushButton, self.cookies_pushButton,
                        self.setting_pushButton]
        self.res_buttons = [self.res_body_pushButton, self.res_cookies_pushButton, self.res_headers_pushButton]
        self.init_ui()
        self.resp_cookie_widget = None
        self.resp_header_widget = None
        self.req_session = RequestSession()

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
        self.api_stackedWidget.addWidget(self.request_set_view)
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
        self.setting_pushButton.clicked.connect(lambda: self.choose_item('setting'))
        self.res_body_pushButton.clicked.connect(lambda: self.choose_item('r_body'))
        self.res_headers_pushButton.clicked.connect(lambda: self.choose_item('r_headers'))
        self.res_cookies_pushButton.clicked.connect(lambda: self.choose_item('r_cookies'))
        self.request_done.connect(self.render_result)
        self.api_url_lineEdit.returnPressed.connect(self.send)

    def render_result(self, list_data):
        self.send_pushButton.setText('Send')
        self.send_pushButton.setEnabled(True)
        self.res_stackedWidget.removeWidget(self.editor)

        # 如果不为空则说明已经请求过则先清理
        if self.resp_cookie_widget is not None:
            self.res_stackedWidget.removeWidget(self.resp_cookie_widget)
            self.res_stackedWidget.removeWidget(self.resp_header_widget)

        if self.editor:
            self.editor.clear()

        if list_data[0]:
            # 获取相应的内容类型, 渲染对应的editor
            resp_type = list_data[1].headers.get('Content-Type', 'html')
            if resp_type.__contains__('html'):
                self.editor = HTMLEditor()
                content = list_data[1].text
            elif resp_type.__contains__('json'):
                self.editor = JSONEditor()
                content = json.dumps(list_data[1].json(), indent=4, ensure_ascii=False, sort_keys=True)

            self.res_stackedWidget.insertWidget(0, self.editor)
            self.editor.setText(content)

            # 显示请求的相关信息
            self.code_label.setText(str(list_data[1].status_code))
            self.code_label.setStyleSheet(f"color:{HTTP_CODE_COLOR.get(list_data[1].status_code)}")
            self.time_label.setText(display_level(list_data[1].elapsed.microseconds, 1000, labels=['us', 'ms', 's'], level=3))
            self.time_label.setStyleSheet(f"color: {HTTP_CODE_COLOR.get(200)}")
            body_size = display_level(int(list_data[1].headers.get('Content-Length', 0)), 1024, labels=['b', 'kb', 'm'],
                                      level=3)
            header_size = display_level(len(str(list_data[1].headers)), 1024, labels=['b', 'kb', 'm'], level=3)
            size = int(list_data[1].headers.get('Content-Length', 0)) + len(str(list_data[1].headers))
            size = display_level(size, 1024, labels=['b', 'kb', 'm'], level=3)
            self.size_label.setText(size)
            self.size_label.setStyleSheet(f'color: {HTTP_CODE_COLOR.get(200)}')
            self.size_label.setToolTip(f'<p>Response Size: {size}</p>'
                                       f'<p style="color: white;">Body Size: {body_size}</p>'
                                       f'<p style="color: white;">Header Size: {header_size}</p>')
            # 显示cookies
            if list_data[1].cookies:
                self.resp_cookie_widget = ResponseTable(
                    headers=['Name', 'Value', 'Domain', 'Path', 'Expires', 'HttpOnly', 'Secure'])
                self.resp_cookie_widget.render_cookies(get_cookies_data(list_data[1].cookies))
                self.res_stackedWidget.addWidget(self.resp_cookie_widget)
            else:
                self.resp_cookie_widget = HintWidget('No cookies yet',
                                                     pix=Icon.COOKIES.value,
                                                     detail='Find all your cookies and their associated domains here.')
                self.res_stackedWidget.addWidget(self.resp_cookie_widget)

            # 显示响应headers
            if list_data[1].headers:
                self.resp_header_widget = ResponseTable()
                self.resp_header_widget.render_data(list_data[1].headers)
                self.res_stackedWidget.addWidget(self.resp_header_widget)
            else:
                self.resp_header_widget = HintWidget('No headers yet')
                self.res_stackedWidget.addWidget(self.resp_header_widget)
            self.res_body_pushButton.click()
        else:
            self.editor = JSONEditor()
            self.res_stackedWidget.insertWidget(0, self.editor)
            self.editor.setText(list_data[2])
            self.code_label.setText('Error')
            self.code_label.setStyleSheet(f"color: red")
            self.time_label.setText('NaN')
            self.time_label.setStyleSheet(f"color: red")
            self.size_label.setText('NaN')
            self.size_label.setStyleSheet(f"color: red")

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
        self.req_session.set_url(api_url)
        self.req_session.max_redirects = int(self.request_set_view.max_redirect_lineEdit.text())
        conn_timeout = self.request_set_view.conn_timeout_lineEdit.text()
        read_timeout = self.request_set_view.read_timeout_lineEdit.text()

        kwargs = {'headers': headers,
                  'timeout': (int(conn_timeout) if conn_timeout != '' else None,
                              int(read_timeout) if read_timeout != '' else None),
                  'allow_redirects': self.request_set_view.redirect,
                  'verify': self.request_set_view.ssl}

        res = self.req_session.send_request(method, **kwargs)
        self.request_done.emit([res.get('result'), res.get('response'), res.get('error_msg')])

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

        elif tag == 'setting':
            update_btn_stylesheet(self.buttons, index=4)
            self.api_stackedWidget.setCurrentIndex(4)

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
    app = QApplication(sys.argv)
    win = ApiView()
    win.show()
    sys.exit(app.exec_())
