"""
# coding:utf-8
@Time    : 2021/07/21
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : config.py
@Desc    : config
@Software: PyCharm
"""
from configparser import ConfigParser
from utils.common import Singleton, basedir


class MyConfig(Singleton):
    def __init__(self, path):
        super(MyConfig, self).__init__()
        self.cfg = ConfigParser()
        self.cfg.read(path)

    def get_all_section(self):
        return self.cfg.sections()

    def read_config(self, section, key):
        return self.cfg.get(section, key)


config = MyConfig(path=basedir + '/resources/conf/base.ini')
