"""
coding:utf-8
file: api_view.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/7/18 20:51
@desc:
"""
from PyQt5.QtWidgets import QWidget, QMessageBox
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog
from src.ui.api_view import Ui_Form
from src.utils.common import update_btn_stylesheet, display_level, \
    get_cookies_data
from src.utils.constants import HTTP_CODE_COLOR, Icon
import json
from src.controller.component.table_view import HeadersTableView, ParamsTableView, ResponseTable
from src.controller.component.qsci_editor import JSONEditor, HTMLEditor
from src.controller.component.hint_view import HintWidget
from src.controller.component.request_set_view import RequestSetView
from src.controller.component.bubble import BubbleLabel
from src.controller.component.request_body_view import RequestBody
from threading import Thread
from PyQt5.QtCore import pyqtSignal
from src.utils.request import RequestSession
from src.utils.models import db, History
import requests
from typing import Optional


class ApiView(Ui_Form, QWidget):
    request_done = pyqtSignal(list)

    def __init__(
            self,
            p_widget: Optional[QWidget] = None
    ):
        super(ApiView, self).__init__()
        self.setupUi(self)
        self.p_widget = p_widget
        self.params_tw = ParamsTableView()
        self.headers_tw = HeadersTableView()
        self.editor = JSONEditor()
        self.request_set_view = RequestSetView()
        self.request_body_view = RequestBody()
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
        self.resp_suffix = 'json'
        self.content = None

    def init_ui(self):
        update_btn_stylesheet(self.buttons, 0)
        update_btn_stylesheet(self.res_buttons, 0)
        self.api_stackedWidget.removeWidget(self.page)
        self.api_stackedWidget.removeWidget(self.page_2)
        self.res_stackedWidget.removeWidget(self.page_3)
        self.res_stackedWidget.removeWidget(self.page_4)
        self.api_stackedWidget.addWidget(self.params_tw)
        self.api_stackedWidget.addWidget(self.headers_tw)
        self.api_stackedWidget.addWidget(self.request_body_view)
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
        self.res_save_pushButton.clicked.connect(self.save_resp)
        self.request_done.connect(self.save_history)

    def save_resp(self):
        """
        将响应数据保存为文件
        """
        name = QFileDialog.getSaveFileName(self, 'Save Response', 'response.' + self.resp_suffix,
                                           filter='"All files (*.*);;html (*.html);;json (*.json)"')
        try:
            if name[0] != '' and self.content:
                filepath = name[0]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(self.content)
                self.show_bubble('文件保存成功!', 'success')
        except Exception:
            self.show_bubble('文件保存失败!', 'danger')

    def show_bubble(
            self,
            msg: str,
            cate: str = 'info'
    ):
        """
        显示提示气泡框
        :param msg: 提示信息内容
        :param cate: 提示类别
        """
        if hasattr(self, "_blabel"):
            self._blabel.stop()
            self._blabel.deleteLater()
            del self._blabel
        self._blabel = BubbleLabel(cate=cate)
        self._blabel.setText(msg)
        self._blabel.show()

    def render_result(
            self,
            list_data: requests.Response
    ):
        """
        将响应数据渲染到对应的控件上
        :param list_data: 响应数据
        """
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
            # 获取数据类型,不同类型实例化不同的编辑器
            resp_type = list_data[1].headers.get('Content-Type', 'html')
            if resp_type.__contains__('html'):
                self.editor = HTMLEditor()
                self.content = list_data[1].text
                self.resp_suffix = 'html'
            elif resp_type.__contains__('json'):
                self.editor = JSONEditor()
                self.content = json.dumps(list_data[1].json(), indent=4, ensure_ascii=False, sort_keys=True)
                self.resp_suffix = 'json'

            self.res_stackedWidget.insertWidget(0, self.editor)
            self.editor.setText(self.content)

            status_code = list_data[1].status_code
            elapsed = list_data[1].elapsed.microseconds
            b_size = list_data[1].headers.get('Content-Length', 0) or len(list_data[1].content)
            h_size = len(str(list_data[1].headers))

            self.render_resp_status(status_code=status_code,
                                    elapsed=elapsed,
                                    b_size=b_size,
                                    h_size=h_size
                                    )
            # 显示响应cookies数据
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

            # 显示相应headers数据
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
        """
        发送请求
        :return: None
        """
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

    def send_request(
            self,
            api_url: str,
            method: str = 'GET',
            headers: Optional[dict] = None
    ):
        """
        时间发送请求方法
        :param api_url: 请求路径
        :param method: 请求方法
        :param headers: 请求头
        """
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
        self.request_done.emit([res.get('result'), res.get('response'), res.get('error_msg'), api_url, headers])

    def choose_item(
            self,
            tag: str
    ):
        """
        切换请求body页面
        :param tag: 页面tag
        """
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

    def save_history(
            self,
            list_data: list
    ):
        """
        将请求历史记录保存到数据库
        :param list_data: 响应数据
        """
        history = History(url=list_data[3],
                          headers=str(list_data[1].headers),
                          status=list_data[1].status_code,
                          elapsed=list_data[1].elapsed.microseconds)
        db.session.add(history)
        db.session.commit()
        from src.controller.workspace_frame import WorkspaceFrame
        self.p_widget: WorkspaceFrame
        self.p_widget.history_view.insert_new_history([list_data[3], history.id])

    def render_resp_status(
            self,
            status_code: int = 200,
            elapsed: str = '',
            b_size: str = '',
            h_size: str = ''
    ):
        """
        渲染响应状态到对应的控件
        :param status_code: 响应码
        :param elapsed: 请求所消耗时间
        :param b_size: body 大小
        :param h_size: header 大小
        """
        self.code_label.setText(str(status_code))
        self.code_label.setStyleSheet(f"color:{HTTP_CODE_COLOR.get(status_code)}")

        self.time_label.setText(
            display_level(elapsed, 1000, labels=['us', 'ms', 's'], level=3))
        self.time_label.setStyleSheet(f"color: {HTTP_CODE_COLOR.get(200)}")

        body_size = display_level(int(b_size), 1024, labels=['b', 'kb', 'm'],
                                  level=3)
        header_size = display_level(h_size, 1024, labels=['b', 'kb', 'm'], level=3)
        size = int(b_size) + int(h_size)
        size = display_level(size, 1024, labels=['b', 'kb', 'm'], level=3)
        self.size_label.setText(size)
        self.size_label.setStyleSheet(f'color: {HTTP_CODE_COLOR.get(200)}')
        self.size_label.setToolTip(f'<p>Response Size: {size}</p>'
                                   f'<p style="color: white;">Body Size: {body_size}</p>'
                                   f'<p style="color: white;">Header Size: {header_size}</p>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ApiView()
    win.show()
    sys.exit(app.exec_())
