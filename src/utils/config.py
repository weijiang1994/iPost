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
from utils.common import basedir
import threading


class MyConfig(object):

    _instance_lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(MyConfig, '_instance'):
            with MyConfig._instance_lock:
                if not hasattr(MyConfig, '_instance'):
                    MyConfig._instance = object.__new__(cls)
        return MyConfig._instance

    def __init__(self, path):
        super(MyConfig, self).__init__()
        self.cfg = ConfigParser()
        self.cfg.read(path)

    def get_all_section(self):
        return self.cfg.sections()

    def read_config(self, section, key):
        return self.cfg.get(section, key)

    def reload(self, path):
        self.cfg.read(path)


config = MyConfig(path=basedir + '/resources/conf/config.ini')
