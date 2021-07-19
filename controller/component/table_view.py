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
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableView, QTableWidgetItem, QCheckBox, QTableWidget
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets


class TableWidget(QTableWidget):
    def __init__(self):
        super(TableWidget, self).__init__()
        self.verticalHeader().setVisible(False)
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(['', '键', '值', '描述'])
        self.setColumnWidth(0, 10)
        # self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def closeEditor(self, editor, hint):
        if hint == QtWidgets.QAbstractItemDelegate.EditNextItem:
            current = self.currentIndex()
            if (current.row() == self.rowCount() - 1 and
                    current.column() == self.columnCount() - 1):
                self.insertRow(self.rowCount())
        super().closeEditor(editor, hint)


class BaseTableView(Ui_Form, QWidget):
    def __init__(self):
        super(BaseTableView, self).__init__()
        self.setupUi(self)
        self.checkBox.clicked.connect(self.set_desc)
        self.verticalLayout.removeWidget(self.tableWidget)
        self.tableWidget = TableWidget()
        self.verticalLayout.addWidget(self.tableWidget)

    def set_desc(self):
        if self.checkBox.isChecked():
            self.tableWidget.setColumnHidden(2, False)
        else:
            self.tableWidget.setColumnHidden(2, True)

    def closeEditor(self, editor, hint):
        if hint == QtWidgets.QAbstractItemDelegate.EditNextItem:
            current = self.currentIndex()
            if (current.row() == self.rowCount() - 1 and
                    current.column() == self.columnCount() - 1):
                self.insertRow(self.rowCount())
        super().closeEditor(editor, hint)


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
