"""
# coding:utf-8
@Time    : 2021/07/17
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : common.py
@Desc    : common
@Software: PyCharm
"""
import os
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
basedir = os.path.dirname(os.path.dirname(__file__))

BUTTON_NORMAL = """
    background-color: transparent;
    border-radius: 0;
"""

BUTTON_SELECTED = """
    background-color: transparent;
    border-radius: 0;
    border-bottom: 2px solid 78c6ee;
"""


def read_qss(path):
    if not os.path.exists(path=path):
        return ''
    with open(path, 'r') as f:
        return f.read()


def update_btn_stylesheet(widgets: list, index=0):
    for idx, widget in enumerate(widgets):
        if idx == index:
            widget.setStyleSheet(BUTTON_SELECTED)
        else:
            widget.setStyleSheet(BUTTON_NORMAL)
        widget.setCursor(QCursor(Qt.PointingHandCursor))
