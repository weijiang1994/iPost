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

basedir = os.path.dirname(os.path.dirname(__file__))
print(basedir)


def read_qss(path):
    if not os.path.exists(path=path):
        return ''
    with open(path, 'r') as f:
        return f.read()
