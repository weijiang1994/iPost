"""
coding:utf-8
file: request_body_view.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/8/14 18:51
@desc:
"""
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QColor
from src.ui.component.request_body_view import Ui_Form
from src.ui.component import body_binary_view
from src.controller.component.message import Message
from src.controller.component.hint_view import HintWidget
from src.controller.component.qsci_editor import TextEditor, JSONEditor, XMLEditor, HTMLEditor, JavaScriptEditor
from PyQt5.Qsci import QsciScintilla


class BodyBinary(QWidget, body_binary_view.Ui_Form):
    def __init__(self):
        super(BodyBinary, self).__init__()
        self.setupUi(self)


class RequestBody(Ui_Form, QWidget):

    def __init__(self):
        super(RequestBody, self).__init__()
        self.setupUi(self)
        self.init_slot()
        self.raw_editor = TextEditor()
        self.js_editor = JavaScriptEditor()
        self.json_editor = JSONEditor()
        self.html_editor = HTMLEditor()
        self.xml_editor = XMLEditor()
        self.body_type = 0
        self.lexers = {
            0: self.raw_editor.lexer,
            1: self.js_editor.lexer,
            2: self.json_editor.lexer,
            3: self.html_editor.lexer,
            4: self.xml_editor.lexer
        }
        self.init_ui()

    def init_slot(self):
        self.none_radioButton.clicked.connect(lambda: self.change_page(0))
        self.form_radioButton.clicked.connect(lambda: self.change_page(1))
        self.raw_radioButton.clicked.connect(lambda: self.change_page(2))
        self.binary_radioButton.clicked.connect(lambda: self.change_page(3))
        self.raw_cate_comboBox.currentIndexChanged.connect(self.set_lexer)
        self.body_stackedWidget.currentChanged.connect(self.data_type)

    def data_type(self):
        self.body_type = self.body_stackedWidget.currentIndex()

    def set_lexer(self, index):
        self.raw_editor.setLexer(self.lexers.get(index))
        self.raw_editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.raw_editor.setMarginWidth(0, '000000')
        self.raw_editor.setMarginsForegroundColor(QColor("#ff888888"))
        self.raw_editor.setMarginsBackgroundColor(QColor('#ff2D2D30'))

    def change_page(self, idx):
        self.raw_cate_comboBox.setVisible(False)
        if idx == 2:
            self.raw_cate_comboBox.setVisible(True)

        self.body_stackedWidget.setCurrentIndex(idx)

    def init_ui(self):
        self.body_stackedWidget.removeWidget(self.page)
        self.body_stackedWidget.removeWidget(self.page_2)
        self.raw_cate_comboBox.setVisible(False)
        self.raw_cate_comboBox.setStyleSheet('color: #5e79fd')
        self.body_stackedWidget.addWidget(HintWidget(msg='This request does not have a body.'))
        self.body_stackedWidget.addWidget(QWidget())
        self.body_stackedWidget.addWidget(self.raw_editor)
        self.body_stackedWidget.addWidget(BodyBinary())
        self.none_radioButton.setChecked(True)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    win = RequestBody()
    win.show()
    sys.exit(app.exec_())
