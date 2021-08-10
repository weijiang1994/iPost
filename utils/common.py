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
from configparser import SafeConfigParser
import threading

basedir = os.path.dirname(os.path.dirname(__file__))


class Singleton(object):
    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, '_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton, '_instance'):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


BUTTON_NORMAL = """
    background-color: transparent;
    border-radius: 0;
    border: none
"""

BUTTON_SELECTED = """
    QPushButton{
        background-color: transparent;
        border-radius: 0;
        border-bottom: 2px solid 78c6ee;
    }
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


def get_conf(path, section):
    pass


def display_level(number: int or float, base: int, labels: list, level: int, round_num=2):
    """
    根据数值大小展现不同等级的label
    :param round_num: 保留几位小数
    :param number: 需要显示的数值
    :param base: 数值基数
    :param labels: 数值单位
    :param level: 显示等级
    :return: render level
    >>> file1 = 1023 # filesize is 1589b
    >>> display_level(file1, base=1024, labels=['b', 'kb', 'm'], level=3)
    >>> '1023b'
    >>> file2 = 4589 # filesize is 4589
    >>> display_level(file2, base=1024, labels=['b', 'kb', 'm'], level=3)
    >>> '4.48kb'
    """
    if level != len(labels):
        raise Exception(f'Label length({len(labels)}) not equal levels number({level}).')
    for i in range(1, level + 1):
        if number < base ** i:
            return str(round(number / base ** (i - 1), round_num)).strip('.0') + str(labels[i - 1])
    if number > base ** level:
        return str(round(number / base ** (level-1), round_num)).strip('.0') + str(labels[-1])


def get_cookies_data(cookies):
    ret = []
    for c in cookies:
        a = [c.name, c.value, c.domain, c.path, c.expires, True if c._rest.get('HttpOnly', False) is None else False, c.secure]
        ret.append(a)
    return ret
