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
import enum

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

HTTP_CODE_COLOR = {200: 'green', 400: 'red', 404: 'red', 403: 'red', 405: 'red', 500: 'red'}


class Icon(enum.Enum):
    ADD_LINE_ICON = basedir + '/resources/images/add-line.png'
    CHECK_LINE = basedir + '/resources/images/check-line.png'
    CLOSE_LINE = basedir + '/resources/images/close-line.png'
    SUBTRACT_LINE = basedir + '/resources/images/subtract-line.png'
    SAVE = basedir + '/resources/images/save.png'
    ALIGN_RIGHT = basedir + '/resources/images/align-right.png'
    ALIGN_LEFT = basedir + '/resources/images/align-left.png'
    ALIGN_CENTER = basedir + '/resources/images/align-center.png'
    LOCATION = basedir + '/resources/images/location.png'
    COOKIES = basedir + '/resources/images/cookies.png'
    TOGGLE_ON = basedir + '/resources/images/toggle-on.png'
    TOGGLE_OFF = basedir + '/resources/images/toggle-off.png'
