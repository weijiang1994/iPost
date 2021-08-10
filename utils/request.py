"""
# coding:utf-8
@Time    : 2021/08/10
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : request.py
@Desc    : request
@Software: PyCharm
"""
from requests import Session


class RequestSession(Session):
    def __init__(self):
        super(RequestSession, self).__init__()
        self.verify = True
        self.max_redirects = 30
        self.url = None

    def set_url(self, url):
        self.url = url

    def send_request(self, method='GET', **kwargs):
        if method.upper() == 'GET':
            self.get(self.url, **kwargs)
        elif method.upper() == 'PUT':
            self.put(self.url, **kwargs)
        elif method.upper() == 'DELETE':
            self.delete(self.url, **kwargs)
        elif method.upper() == 'POST':
            self.post(self.url, **kwargs)
