"""
# coding:utf-8
@Time    : 2021/11/16
@Author  : jiangwei
@File    : mai.py
@Desc    : mai
@email   : qq804022023@gmail.com
@Software: PyCharm
"""
from flask import Flask, request

token = '2f85a31c-46ac-11ec-9183-8742b40cb09a'
app = Flask(__name__)


@app.route('/test-param')
def test_param():
    key1 = request.args.get('key1')
    key2 = request.args.get('key2')
    return {'key1': key1, 'key2': key2}


@app.route('/test-headers')
def test_headers():
    token1 = request.headers.get('token')
    if token1 != token:
        return {'code': 500, 'msg': 'Token is error!'}
    return {'code': 200, 'msg': 'Authorize Successful!'}


@app.route('/test-json', methods=['POST'])
def test_json():
    print('json is ', request.json)
    print('form is ', request.form)
    print('value is ', request.values)
    print('cookie is ', request.cookies)
    print('args is ', request.args)
    print('data is ', request.data)
    print(request.get_data())
    return request.json if request.json else {'code': '500', 'msg': 'Not send json data.'}


if __name__ == '__main__':
    app.run(debug=True)
