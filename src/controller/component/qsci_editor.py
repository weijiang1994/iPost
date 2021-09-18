"""
coding:utf-8
file: qsci_editor.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2021/8/2 22:16
@desc:
"""
from PyQt5.Qsci import QsciLexerJSON, QsciScintilla, QsciLexerHTML, QsciLexerJavaScript, QsciLexerXML, \
    QsciLexerCustom, QsciLexerTeX
from PyQt5.QtGui import QColor, QFont


class BaseEditor(QsciScintilla):
    def __init__(self):
        super(BaseEditor, self).__init__()
        self.font = QFont()
        self.font.setFamily('Consolas')
        self.font.setPointSize(10)
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

        # set auto complete
        self.setAutoCompletionCaseSensitivity(False)
        self.setAutoCompletionReplaceWord(False)
        self.setAutoCompletionSource(QsciScintilla.AcsDocument)
        self.setAutoCompletionThreshold(1)


class JSONEditor(BaseEditor):
    def __init__(self):
        super(JSONEditor, self).__init__()
        self.lexer = QsciLexerJSON(self)
        self.lexer.setFont(self.font)
        self.setLexer(self.lexer)
        self.lexer.setDefaultPaper(QColor('#2D2D30'))
        self.lexer.setPaper(QColor('#2D2D30'))
        self.lexer.setColor(QColor('#5AB8F7'), QsciLexerJSON.Property)
        self.lexer.setColor(QColor("#99C38E"), QsciLexerJSON.Number)
        self.lexer.setColor(QColor('#C87F4F'), QsciLexerJSON.String)
        self.lexer.setColor(QColor('#EA4F4F'), QsciLexerJSON.Error)
        self.lexer.setColor(QColor("#FFFFFF"), QsciLexerJSON.Operator)
        self.lexer.setColor(QColor('#C87F4F'), QsciLexerJSON.IRI)
        self.lexer.setColor(QColor('#C87F4F'), QsciLexerJSON.IRICompact)


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
        self.lexer.setColor(QColor('#F92672'), QsciLexerHTML.JavaScriptKeyword)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerHTML.JavaScriptWord)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerHTML.JavaScriptSymbol)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerHTML.JavaScriptDefault)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerHTML.JavaScriptNumber)
        self.lexer.setColor(QColor('#72D02C'), QsciLexerHTML.JavaScriptDoubleQuotedString)
        self.lexer.setColor(QColor('#72D02C'), QsciLexerHTML.JavaScriptSingleQuotedString)


class JavaScriptEditor(BaseEditor):
    def __init__(self):
        super(JavaScriptEditor, self).__init__()
        self.lexer = QsciLexerJavaScript(self)
        self.lexer.setFont(self.font)
        self.setLexer(self.lexer)
        self.lexer.setDefaultPaper(QColor('#2D2D30'))
        self.lexer.setPaper(QColor('#2D2D30'))

        self.lexer.setColor(QColor('#43BCDD'), QsciLexerJavaScript.Keyword)
        self.lexer.setColor(QColor('#C1CF57'), QsciLexerJavaScript.DoubleQuotedString)
        self.lexer.setColor(QColor('#C1CF57'), QsciLexerJavaScript.SingleQuotedString)
        self.lexer.setColor(QColor('#7E714C'), QsciLexerJavaScript.CommentLine)
        self.lexer.setColor(QColor('#528EE9'), QsciLexerJavaScript.Identifier)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerJavaScript.Operator)


class XMLEditor(BaseEditor):
    def __init__(self):
        super(XMLEditor, self).__init__()
        self.lexer = QsciLexerXML(self)
        self.lexer.setFont(self.font)
        self.setLexer(self.lexer)
        self.lexer.setDefaultPaper(QColor('#2D2D30'))
        self.lexer.setPaper(QColor('#2D2D30'))

        self.lexer.setColor(QColor('#4594B4'), QsciLexerXML.Tag)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerXML.Default)
        self.lexer.setColor(QColor('#C88351'), QsciLexerXML.HTMLDoubleQuotedString)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerXML.PHPOperator)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerXML.PythonOperator)
        self.lexer.setColor(QColor('#4594B4'), QsciLexerXML.XMLTagEnd)
        self.lexer.setColor(QColor('#88C4E2'), QsciLexerXML.Attribute)


class TextEditor(BaseEditor):
    def __init__(self):
        super(TextEditor, self).__init__()
        self.lexer = QsciLexerTeX(self)
        self.lexer.setFont(self.font)
        self.setLexer(self.lexer)
        self.lexer.setDefaultPaper(QColor('#2D2D30'))
        self.lexer.setPaper(QColor('#2D2D30'))
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerTeX.Command)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerTeX.Default)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerTeX.Group)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerTeX.Special)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerTeX.Symbol)
        self.lexer.setColor(QColor('#FFFFFF'), QsciLexerTeX.Text)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
    import sys

    app = QApplication(sys.argv)
    win = QWidget()
    l1 = QLabel('HTML Editor')
    l2 = QLabel('JSON Editor')
    l3 = QLabel('JavaScript Editor')
    l4 = QLabel('XML Editor')
    v_layout = QVBoxLayout()
    json_editor = JSONEditor()
    html_editor = HTMLEditor()
    js_editor = JavaScriptEditor()
    xml_editor = XMLEditor()

    html_editor.setText("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sample-default theme</title>
    {{ githubcard.init_css() }}
    {{ githubcard.init_js() }}
    <style>
        .username{
            color: "#123456"
        }
    </style>
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
<script>
    function call(){
        console.log("I am Ironman.")
        let a = 123;
        console.log('hello' + a);
        var a = 123;
        for(i=0;i++;i<20){
            console.log(i);
        }
    }
</script>
</body>
</html>
    """)
    json_editor.setText("""{
    "code": 200,
    "result": [
        {
            "hits": "29",
            "title": "你可以像只猪一样懒，却无法像只猪一样，懒得心安理得。"
        }
    ]
}
    """)
    js_editor.setText("""function test(){
    let abc = 123;
    console.log('SingleQuotedString')
    console.log("DoubleQuotedString")
    // Hello, world!
    /* 
    Doc Comment
    */
}
    """)
    xml_editor.setText("""<id>42</id>
<title>Blogin</title>
<updated>2021-09-18T06:16:46.508252+00:00</updated>
<link href="https://2dogz.cn"/>
<generator uri="https://lkiesow.github.io/python-feedgen" version="0.9.0">python-feedgen</generator>
<subtitle>
Blogin是一个个人博客网站，后端使用Flask框架，前端使用Bootstrap4，主要分享一些编程类的技术以及一些陈词滥调的文章!
</subtitle>
    """)
    v_layout.addWidget(l1)
    v_layout.addWidget(html_editor)
    v_layout.addWidget(l2)
    v_layout.addWidget(json_editor)
    v_layout.addWidget(l3)
    v_layout.addWidget(js_editor)
    v_layout.addWidget(l4)
    v_layout.addWidget(xml_editor)
    win.setLayout(v_layout)
    win.setGeometry(0, 0, 1030, 800)
    win.show()
    sys.exit(app.exec_())
