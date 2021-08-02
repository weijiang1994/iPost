"""
coding:utf-8
file: JsonEditor.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/8/2 22:16
@desc:
"""
from PyQt5.Qsci import QsciLexerJSON, QsciScintilla
from PyQt5.QtGui import QColor, QFont


class JSONEditor(QsciScintilla):
    def __init__(self):
        super(JSONEditor, self).__init__()
        self.font = QFont()
        self.font.setPointSize(14)
        self.setFont(self.font)
        self.setWrapMode(QsciScintilla.WrapWord)
        self.setWrapVisualFlags(QsciScintilla.WrapFlagNone)
        self.setTabWidth(4)
        self.setIndentationGuides(True)
        self.setAutoIndent(True)
        self.setCaretForegroundColor(QColor('#ff0000ff'))
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor('#E0E0FF'))
        self.setCaretWidth(2)
        self.setMinimumHeight(300)

        # set number margin style
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, '0000')
        self.setMarginsForegroundColor(QColor("#ff888888"))

        # set folding margin style
        self.setMarginType(1, QsciScintilla.TextMargin)
        self.setMarginWidth(1, '00000')

        self.lexer = QsciLexerJSON(self)
        self.lexer.setFont(self.font)
        self.setLexer(self.lexer)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = JSONEditor()
    win.show()
    sys.exit(app.exec_())
