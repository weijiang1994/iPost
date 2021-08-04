"""
coding:utf-8
file: json_editor.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/8/2 22:16
@desc:
"""
from PyQt5.Qsci import QsciLexerJSON, QsciScintilla
from PyQt5.QtGui import QColor, QFont
from utils.constants import VSS_DARK_THEME_PATH
from utils.common import read_qss


class JSONEditor(QsciScintilla):
    def __init__(self):
        super(JSONEditor, self).__init__()
        self.font = QFont()
        self.font.setPointSize(12)
        self.setWrapMode(QsciScintilla.WrapWord)
        self.setWrapVisualFlags(QsciScintilla.WrapFlagNone)
        self.setTabWidth(4)
        self.setIndentationGuides(True)
        self.setIndentationGuidesBackgroundColor(QColor())
        self.setAutoIndent(True)
        self.setCaretForegroundColor(QColor('#eeb12d'))
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor('#151515'))
        self.setCaretWidth(2)

        # set number margin style
        self.setMarginType(0, QsciScintilla.NumberMargin)
        self.setMarginWidth(0, '000000')
        self.setMarginsForegroundColor(QColor("#ff888888"))
        self.setMarginsBackgroundColor(QColor('#ff2D2D30'))

        # set folding through the indentation
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle)
        self.setFoldMarginColors(QColor('#ff2D2D30'), QColor('#ff2D2D30'))

        # set JSON lexer
        self.lexer = QsciLexerJSON(self)
        self.lexer.setFont(self.font)
        self.setLexer(self.lexer)
        self.lexer.setDefaultPaper(QColor('#2D2D30'))
        self.lexer.setPaper(QColor('#2D2D30'))


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = JSONEditor()
    win.show()
    sys.exit(app.exec_())
