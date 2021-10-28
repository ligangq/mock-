# author:lee:2021/8/24 0024 11:37
'''
mock 挡板
作用：保证测试业务顺利进行。流程是通畅且稳定的
场景：1.调用第三方接口，
2.透传  需要享受接口原本的功能，还需要提供接口不存在（未开发完成）的功能


需求：登录接口没有黑名单功能
todo 1.做一个mock服务，实现黑名单功能
todo 2.这个登录接口原有功能需要保留（登录成功）--透传    study_passTrough.py

'''
from flask import Flask, request, jsonify

from Testfan.api.study_passThrough import passThroughLo, passThroughRe

app = Flask(__name__)
# 响应里面识别中文，做如下更改
app.config['JSON_AS_ASCII'] = False
# 添加登录路由，实现mock功能
@app.route('/login/mock',methods = ['POST'])
def login():
    '''
    实现黑名单的功能
    :return:
    '''
    data = request.get_json()

    if data.get('name') ==  '黑名单':
        return jsonify({'data': data, 'message': '该客户为黑名单', 'code': 200})
    else:
        # 不走黑名单的mock服务，走原来的功能
        resq = passThroughLo(data)
        return resq

# 透传
# 为什么要实现一个透传功能？  不用起两个服务
@app.route('/<func>',methods = ['POST'])
def register(func):
    # 判断条件：前端传进来的参数
    data = request.get_json()
    if func == 'register':
        # 透传注册功能
        resp = passThroughRe(data)
        return resp

if __name__ == '__main__':
    app.run(debug=True,port=9999)
