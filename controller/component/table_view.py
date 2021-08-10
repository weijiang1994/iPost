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
from utils.constants import HEADER_ITEMS, Icon, VSS_DARK_THEME_PATH
from utils.common import read_qss
from PyQt5.QtWidgets import QWidget, QHeaderView, QTableView, QTableWidgetItem, QCheckBox, QTableWidget, QLineEdit, \
    QCompleter, QMenu, QAction
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QIcon
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QApplication, QHeaderView, QStyle, QStyleOptionButton, QTableView)
from PyQt5.QtCore import (pyqtSignal, Qt, QAbstractTableModel, QModelIndex, QRect, QVariant)

completer = QCompleter(HEADER_ITEMS)
completer.setFilterMode(Qt.MatchContains)
completer.setCompletionMode(QCompleter.PopupCompletion)


class TableWidget(QTableWidget):
    def __init__(self):
        super(TableWidget, self).__init__()
        self.verticalHeader().setVisible(False)
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['KEY', 'VALUE', 'DESC'])
        self.setColumnWidth(0, 10)
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def closeEditor(self, editor, hint):
        if hint == QtWidgets.QAbstractItemDelegate.EditNextItem:
            current = self.currentIndex()
            if current.row() == self.rowCount() - 1 and current.column() == self.columnCount() - 1:
                self.insertRow(self.rowCount())
                qle = QLineEdit('')
                qle.setStyleSheet('border: none')
                qle.setCompleter(completer)
                self.setCellWidget(self.rowCount() - 1, 0, qle)
        super().closeEditor(editor, hint)


class BaseTableView(Ui_Form, QWidget):
    def __init__(self):
        super(BaseTableView, self).__init__()
        self.setupUi(self)
        self.checkBox.clicked.connect(self.set_desc)
        self.verticalLayout.removeWidget(self.tableWidget)
        self.tableWidget = TableWidget()
        self.verticalLayout.addWidget(self.tableWidget)
        self.label.setText('Query')
        self.checkBox.setText('Description')

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
        self.label.setText('Headers')
        self.headers = [['User-Agent', 'iPost Runtime v1.0.23', ''],
                        ['Accept', '*/*', ''],
                        ['Accept-Encoding', 'gzip, deflate, br', ''],
                        ['Connection', 'keep alive', '']]
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.right_btn_menu)
        self.unselect_row = []
        self.init_data()

    def right_btn_menu(self, pos):
        row_num = -1
        for i in self.tableWidget.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num == -1:
            return
        menu = QMenu()
        menu.setStyleSheet(read_qss(VSS_DARK_THEME_PATH))
        menu.setProperty('class', 'sub-menu')
        select = QAction('选择参数')
        unselect = QAction('去除参数')
        delete = QAction('删除参数')
        add = QAction('新增参数')
        select.setIcon(QIcon(Icon.CHECK_LINE.value))
        unselect.setIcon(QIcon(Icon.CLOSE_LINE.value))
        delete.setIcon(QIcon(Icon.SUBTRACT_LINE.value))
        add.setIcon(QIcon(Icon.ADD_LINE_ICON.value))
        for action in [select, unselect, delete, add]:
            menu.addAction(action)
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == select:
            _row = self.tableWidget.currentRow()
            if _row not in self.unselect_row:
                return
            else:
                self.unselect_row.remove(_row)
                self.update_item_bg(_row, bg_color='#2D2D30')

        elif action == unselect:
            _row = self.tableWidget.currentRow()
            if _row not in self.unselect_row:
                self.unselect_row.append(_row)
                self.update_item_bg(_row, bg_color='#383939')
            else:
                return

        elif action == delete:
            _row = self.tableWidget.currentRow()
            if _row in self.unselect_row:
                self.unselect_row.remove(_row)
            elif len(self.unselect_row):
                for idx, row in enumerate(self.unselect_row):
                    if row > _row:
                        self.unselect_row[idx] = row - 1

            self.tableWidget.removeRow(self.tableWidget.currentRow())

        elif action == add:
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            qle = QLineEdit('')
            qle.setStyleSheet('border: none')
            qle.setCompleter(completer)
            self.tableWidget.setCellWidget(self.tableWidget.rowCount() - 1, 0, qle)

    def update_item_bg(self, _row, bg_color):
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(_row, col) or self.tableWidget.cellWidget(_row, col)
            if type(item) is QTableWidgetItem:
                item.setBackground(QBrush(QColor(bg_color)))
            if type(item) is QLineEdit:
                item.setStyleSheet(f'background-color: {bg_color};border:none')

    def init_data(self):
        for i in range(len(self.headers)):
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            item = self.headers[i]
            for j in range(len(item)):
                if j == 0:
                    qle = QLineEdit(str(self.headers[i][j]))
                    qle.setStyleSheet('border: none')
                    qle.setCompleter(completer)
                    self.tableWidget.setCellWidget(i, j, qle)
                else:
                    item = QTableWidgetItem(str(self.headers[i][j]))
                    self.tableWidget.setItem(i, j, item)


class ResponseTable(QTableWidget):
    def __init__(self, headers=None):
        super(ResponseTable, self).__init__()
        self.set_headers(headers)
        self.verticalHeader().setVisible(False)
        self.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def set_headers(self, headers=None):
        if headers is None:
            headers = ['Key', 'Value']
        self.setColumnCount(len(headers))
        self.setHorizontalHeaderLabels(headers)

    def render_data(self, datas):
        for key in datas:
            self.insertRow(self.rowCount())
            k_item = QTableWidgetItem(key)
            v_item = QTableWidgetItem(datas.get(key))
            self.setItem(self.rowCount() - 1, 0, k_item)
            self.setItem(self.rowCount() - 1, 1, v_item)

    def render_cookies(self, cookies):
        for r_index, cookie in enumerate(cookies):
            self.insertRow(self.rowCount())
            for c_index, c in enumerate(cookie):
                item = QTableWidgetItem(str(c))
                self.setItem(r_index, c_index, item)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = HeadersTableView()
    win.show()
    sys.exit(app.exec_())
