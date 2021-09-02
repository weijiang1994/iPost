"""
# coding:utf-8
@Time    : 2021/08/13
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : bubble.py
@Desc    : Bubble
@Software: PyCharm
"""
from PyQt5.QtGui import QPainter, QPainterPath, QColor, QPen
from PyQt5.QtCore import (QRectF, Qt, QPropertyAnimation, pyqtProperty,
                          QPoint, QParallelAnimationGroup, QEasingCurve)
from PyQt5.QtWidgets import (QLabel, QWidget, QVBoxLayout, QApplication,
                             QLineEdit, QPushButton)
from src.utils.constants import LEVELBG


class BubbleLabel(QWidget):
    def __init__(self, cate='info', *args, **kwargs):
        text = kwargs.pop("text", "")
        super(BubbleLabel, self).__init__(*args, **kwargs)
        self.setWindowFlags(
            Qt.Window | Qt.Tool | Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint)
        self.bg_color = QColor(LEVELBG.get(cate.lower(), 'info'))
        self.bd_color = QColor(LEVELBG.get(cate.lower(), 'info'))

        # Set minimum width and height
        self.setMinimumWidth(200)
        self.setMinimumHeight(58)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        layout = QVBoxLayout(self)
        # Top left and bottom right margins (16 below because triangles are included)
        layout.setContentsMargins(8, 8, 8, 16)
        self.label = QLabel(self)
        self.label.setStyleSheet('color: white;')
        layout.addWidget(self.label)
        self.setText(text)
        # Get screen height and width
        self._desktop = QApplication.instance().desktop()

    def setText(self, text):
        self.label.setText(text)

    def text(self):
        return self.label.text()

    def stop(self):
        self.hide()
        self.animationGroup.stop()
        self.close()

    def show(self):
        super(BubbleLabel, self).show()
        # Window start position
        startPos = QPoint(
            self._desktop.screenGeometry().width() - self.width(),
            self._desktop.availableGeometry().height() - self.height())
        endPos = QPoint(
            self._desktop.screenGeometry().width() - self.width(),
            self._desktop.availableGeometry().height() - self.height() * 3 - 5)
        self.move(startPos)
        # Initialization animation
        self.initAnimation(startPos, endPos)

    def initAnimation(self, startPos, endPos):
        # Transparency animation
        opacityAnimation = QPropertyAnimation(self, b"opacity")
        opacityAnimation.setStartValue(1.0)
        opacityAnimation.setEndValue(0.0)
        # Set the animation curve
        opacityAnimation.setEasingCurve(QEasingCurve.Linear)
        opacityAnimation.setDuration(2000)
        # Moving up animation
        moveAnimation = QPropertyAnimation(self, b"pos")
        moveAnimation.setStartValue(startPos)
        moveAnimation.setEndValue(endPos)
        moveAnimation.setEasingCurve(QEasingCurve.InQuad)
        moveAnimation.setDuration(2000)
        # Parallel animation group (the purpose is to make the two animations above simultaneously)
        self.animationGroup = QParallelAnimationGroup(self)
        self.animationGroup.addAnimation(opacityAnimation)
        self.animationGroup.addAnimation(moveAnimation)
        # Close window at the end of the animation
        self.animationGroup.finished.connect(self.close)
        self.animationGroup.start()

    def paintEvent(self, event):
        super(BubbleLabel, self).paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Antialiasing

        rectPath = QPainterPath()  # Rounded Rectangle
        triPath = QPainterPath()  # Bottom triangle

        height = self.height() - 8  # Offset up 8
        rectPath.addRoundedRect(QRectF(0, 0, self.width(), height), 5, 5)
        x = self.width() / 5 * 4
        triPath.moveTo(x, height)  # Move to the bottom horizontal line 4/5
        # Draw triangle
        triPath.lineTo(x + 6, height + 8)
        triPath.lineTo(x + 12, height)

        rectPath.addPath(triPath)  # Add a triangle to the previous rectangle

        # Border brush
        painter.setPen(QPen(self.bd_color, 1, Qt.SolidLine,
                            Qt.RoundCap, Qt.RoundJoin))
        # Background brush
        painter.setBrush(self.bg_color)
        # Draw shape
        painter.drawPath(rectPath)
        # Draw a line on the bottom of the triangle to ensure the same color as the background
        painter.setPen(QPen(self.bg_color, 1,
                            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(x, height, x + 12, height)

    def windowOpacity(self):
        return super(BubbleLabel, self).windowOpacity()

    def setWindowOpacity(self, opacity):
        super(BubbleLabel, self).setWindowOpacity(opacity)

    # Since the opacity property is not in QWidget, you need to redefine one
    opacity = pyqtProperty(float, windowOpacity, setWindowOpacity)


class TestWidget(QWidget):

    def __init__(self, *args, **kwargs):
        super(TestWidget, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)
        self.msgEdit = QLineEdit(self, returnPressed=self.onMsgShow)
        self.msgEdit.setText('HELLO')
        self.msgButton = QPushButton("Display content", self, clicked=self.onMsgShow)
        layout.addWidget(self.msgEdit)
        layout.addWidget(self.msgButton)

    def onMsgShow(self):
        msg = self.msgEdit.text().strip()
        if not msg:
            return
        if hasattr(self, "_blabel"):
            self._blabel.stop()
            self._blabel.deleteLater()
            del self._blabel
        self._blabel = BubbleLabel(cate='danger')
        self._blabel.setText(msg)
        self._blabel.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = TestWidget()
    w.show()
    sys.exit(app.exec_())