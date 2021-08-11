"""
coding:utf-8
file: qsci_editor.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/8/2 22:16
@desc:
"""
from PyQt5.Qsci import QsciLexerJSON, QsciScintilla, QsciLexerHTML
from PyQt5.QtGui import QColor, QFont
from utils.constants import VSS_DARK_THEME_PATH
from utils.common import read_qss


class BaseEditor(QsciScintilla):
    def __init__(self):
        super(BaseEditor, self).__init__()
        self.font = QFont()
        self.font.setFamily('Consolas')
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


class JSONEditor(BaseEditor):
    def __init__(self):
        super(JSONEditor, self).__init__()
        self.lexer = QsciLexerJSON(self)
        self.lexer.setFont(self.font)
        self.setLexer(self.lexer)
        self.lexer.setDefaultPaper(QColor('#2D2D30'))
        self.lexer.setPaper(QColor('#2D2D30'))


class HTMLEditor(BaseEditor):
    def __init__(self):
        super(HTMLEditor, self).__init__()
        self.lexer = QsciLexerHTML(self)
        self.lexer.setFont(self.font)
        self.setLexer(lexer=self.lexer)
        self.lexer.setDefaultPaper(QColor('#2D2D30'))
        self.lexer.setPaper(QColor('#2D2D30'))

        self.lexer.setColor(QColor('#D12654'), QsciLexerHTML.Tag)
        self.lexer.setColor(QColor('#72D02C'), QsciLexerHTML.HTMLDoubleQuotedString)
        self.lexer.setColor(QColor('#B071CF'), QsciLexerHTML.Attribute)
        self.lexer.setColor(QColor('#75715A'), QsciLexerHTML.UnknownTag)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerHTML.Default)
        self.lexer.setColor(QColor('#eeeeee'), QsciLexerHTML.SGMLCommand)
        self.lexer.setColor(QColor('#75715A'), QsciLexerHTML.JavaScriptKeyword)

        for i in range(100):
            # print(self.lexer.defaultColor(i).getRgb())
            if self.lexer.defaultColor(i).getRgb() == (0, 0, 128, 255):
                print(i)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
    import sys

    app = QApplication(sys.argv)
    win = QWidget()
    l1 = QLabel('HTML Editor')
    l2 = QLabel('JSON Editor')
    v_layout = QVBoxLayout()
    json_editor = JSONEditor()
    html_editor = HTMLEditor()
    html_editor.setText("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample-default theme</title>
    {{ githubcard.init_css() }}
    {{ githubcard.init_js() }}
</head>
<body>
<div class="container mt-2">
    <h4><b>Flask-GithubCard extension sample.</b></h4>
    <hr>
    <a href="/default/">default</a>
    <a href="/darkly/">darkly</a>
    <div class="container mt-2">
        <div class="row ">
            <div class="col-4">{{ githubcard.generate_card() }}</div>
        </div>
    </div>
</div>
</body>
</html>
    """)
    v_layout.addWidget(l1)
    v_layout.addWidget(html_editor)
    v_layout.addWidget(l2)
    v_layout.addWidget(json_editor)
    win.setLayout(v_layout)
    win.setGeometry(0, 0, 600, 400)
    win.show()
    sys.exit(app.exec_())
