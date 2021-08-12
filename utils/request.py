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
import traceback


class RequestSession(Session):
    def __init__(self, url='https://2dogz.cn/api/get-soul?counts=10'):
        super(RequestSession, self).__init__()
        self.verify = True
        self.max_redirects = 30
        self._url = url
        self._res = None

    def set_url(self, url):
        self._url = url

    def send_request(self, method='GET', **kwargs):
        self._res = None
        try:
            # if method.upper() == 'GET':
            #     self._res = self.get(self._url, **kwargs)
            # elif method.upper() == 'PUT':
            #     self._res = self.put(self._url, **kwargs)
            # elif method.upper() == 'DELETE':
            #     self._res = self.delete(self._url, **kwargs)
            # elif method.upper() == 'POST':
            #     self._res = self.post(self._url, **kwargs)
            self._res = self.request(url=self._url, method=method, **kwargs)
            return {'result': True, 'response': self._res, 'error_msg': ''}
        except Exception:
            return {'result': False, 'response': self._res, 'error_msg': str(traceback.format_exc())}


if __name__ == '__main__':

    a = {'headers': {'Access-Username': 'jiangwei1994', 'Access-Token': 'mMS2Dy7nGwVQt8649XU0rZ5gRbNuca3W'},
         'timeout': (None, 20)}
    rs = RequestSession(url='http://127.0.0.1:8008/check_activation?z=213131&f=2314214412')
    res = rs.send_request(method='get', **a)

    if res.get('result'):
        print(res.get('response').status_code)
        print(res.get('response').headers)
        print(res.get('response').cookies)
        print(res.get('response').json())
    else:
        print(res.get('error_msg'))
