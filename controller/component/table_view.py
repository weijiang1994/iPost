"""
# coding:utf-8
@Time    : 2021/07/19
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : table_view.py
@Desc    : table_view
@Software: PyCharm
"""
from ui.component.query_params_view import Ui_Form
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableView, QTableWidgetItem, QCheckBox
from PyQt5 import QtCore


class BaseTableView(Ui_Form, QWidget):
    def __init__(self):
        super(BaseTableView, self).__init__()
        self.setupUi(self)
        self.checkBox.clicked.connect(self.set_desc)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def set_desc(self):
        if self.checkBox.isChecked():
            self.tableWidget.setColumnHidden(2, False)
        else:
            self.tableWidget.setColumnHidden(2, True)


class ParamsTableView(BaseTableView):
    def __init__(self):
        super(ParamsTableView, self).__init__()


class HeadersTableView(BaseTableView):
    def __init__(self):
        super(HeadersTableView, self).__init__()
        self.label.setText('请求头')
        self.headers = [['Host', 'localhost', '请求主机'],
                        ['User-Agent', 'iPost Runtime v1.0.23', ''],
                        ['Accept', '*/*', ''],
                        ['Accept-Encoding', 'gzip, deflate, br', ''],
                        ['Connection', 'keep alive', '']]
        self.init_data()

    def init_data(self):
        for i in range(len(self.headers)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            item = self.headers[i]
            for j in range(len(item)):
                item = QTableWidgetItem(str(self.headers[i][j]))
                if j == 0:
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.CheckState.Checked)
                self.tableWidget.setItem(i, j, item)
