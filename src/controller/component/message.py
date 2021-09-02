"""
# coding:utf-8
@Time    : 2021/08/27
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : message.py
@Desc    : message
@Software: PyCharm
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QDesktopWidget
from PyQt5 import QtCore
from PyQt5 import QtGui


class Message(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Message, self).__init__()
        self.parent = parent
        self.setStyle(QtWidgets.QStyleFactory.create("plastique"))
        self.setWindowOpacity(0.98)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.frame = QtWidgets.QFrame()
        self.frame_layout = QtWidgets.QHBoxLayout()
        self.frame_layout.setSpacing(25)
        self.frame_layout.setContentsMargins(15, 15, 15, 15)
        self.frame.setLayout(self.frame_layout)

        self.btn = QtWidgets.QPushButton("x")
        self.btn.clicked.connect(self.close)
        self.btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.label = QtWidgets.QLabel()
        self.frame_layout.addWidget(self.label)
        self.frame_layout.addWidget(self.btn)
        self.main_layout.addWidget(self.frame)

    def center(self):
        qr = self.frameGeometry()
        print(self.geometry())
        print(qr)
        if not self.parent:
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        else:
            pp = self.parent.geometry().center()
            self.move(pp)

    def info(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #7cd1ef;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 18px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #6cbddc;
                }

                QLabel{
                    color: #31708f;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def success(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #b9df90;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 17px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #a0c97f;
                }

                QLabel{
                    color: #3c763d;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def warning(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #ffdd87;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 18px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #e8c677;
                }

                QLabel{
                    color: #8a6d3b;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def error(self, msg):
        self.setStyleSheet("""
                QFrame{
                    color: black;
                    background-color: #f2838f;
                    border-radius: 5px;
                }

                QPushButton {
                    border: 0px solid rgba(255, 255, 255, 0);
                    font-size: 18px;
                    font-family: "Microsoft YaHei";
                    color: rgba(255, 255, 255, 255);
                    padding-bottom: 5px;
                }

                QPushButton:pressed {
                    color: #c16872;
                }

                QLabel{
                    color: #b44e4f;
                    font-weight: 700;
                    font-size: 14px;
                    font-family: "Microsoft YaHei";
                }
                """)

        self.label.setText(msg)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

    def show(self) -> None:
        self.center()
        super().show()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    win = Message()
    win.info('白日依山尽，黄河入海流。')
    win.show()
    sys.exit(app.exec_())
