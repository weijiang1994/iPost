"""
# coding:utf-8
@Time    : 2021/07/22
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : constants.py
@Desc    : constant
@Software: PyCharm
"""
from utils.common import basedir

BASE_CONFIG_PATH = basedir + '/resources/conf/base.ini'
VSS_DARK_THEME_PATH = basedir + '/resources/vss-dark.qss'
MATERIAL_THEME_PATH = basedir + '/resources/material.qss'
HEADER_ITEMS = ['Accept-Encoding', 'Accept-Charset', 'Accept-Language', 'Access-Control-Request-Headers',
                'Access-Control-Request-Method', 'Authorization', 'Cache-Control', 'Content-MD5', 'Content-Length',
                'Content-Transfer-Encoding', 'Content-Type', 'Cookie', 'Cookie2', 'Date', 'Expect', 'From', 'Host',
                'Access-Username', 'Access-Token'
                ]

TABLE_ITEM_UNSELECT_BGCOLOR = {'vs-dark': '#383939'}
TABLE_ITEM_SELECT_BGCOLOR = {'vs-dark': '#2D2D30'}
