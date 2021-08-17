"""
# coding:utf-8
@Time    : 2021/08/16
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : history_view.py
@Desc    : history_view
@Software: PyCharm
"""
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem
from ui.component.history_view import Ui_Form
from utils.models import db, History
import threading
import datetime


class MyTreeWidgetItem(QTreeWidgetItem):
    def __init__(self):
        super().__init__()
        self.id = None


class HistoryView(QWidget, Ui_Form):
    query_data_done = pyqtSignal(bool, str, list)

    def __init__(self):
        super(HistoryView, self).__init__()
        self.setupUi(self)
        self.finished = False
        self.data = {}
        self.root_list = []
        self.init_data()
        self.init_slot()
        self.init_ui()

    def init_ui(self):
        self.hint_label.setText('Loading Data...')
        self.history_treeWidget.setVisible(False)
        self.history_treeWidget.setHeaderHidden(True)
        self.history_treeWidget.setColumnCount(1)

    def init_slot(self):
        self.query_data_done.connect(self.query_done)
        self.history_treeWidget.itemClicked.connect(self.tree_item_click)

    def tree_item_click(self, item, column):
        if isinstance(item, MyTreeWidgetItem):
            ret = db.session.query(History).filter_by(id=item.id).first()
            self.query_data_done.emit(True, 'history', [ret])

    def init_data(self):
        th = threading.Thread(target=self.query_data)
        th.start()

    def query_done(self, _, cate):
        self.finished = True
        if self.data and cate == 'init':
            self.hint_label.setVisible(False)
            self.history_treeWidget.setVisible(True)
            self.render_tree()
        else:
            self.hint_label.setText('No History Data')

    def render_tree(self):
        for key in self.data:
            root = QTreeWidgetItem()
            root.setText(0, key)
            self.root_list.append(root)
            for url in self.data.get(key):
                child = MyTreeWidgetItem()
                child.setToolTip(0, url[0])
                child.setText(0, url[0])
                child.id = url[1]
                root.addChild(child)
        self.history_treeWidget.insertTopLevelItems(0, self.root_list)

    def query_data(self):
        try:
            histories = db.session.query(History).order_by(History.c_time.desc()).all()
            for history in histories:
                day = history.c_time.strftime('%Y-%m-%d')
                if day not in self.data.keys():
                    self.data[day] = [[history.url, history.id]]
                else:
                    self.data[day].append([history.url, history.id])
            self.query_data_done.emit(True, 'init', [])
        except Exception:
            import traceback
            self.query_data_done.emit(False, 'init', [traceback.format_exc()])
