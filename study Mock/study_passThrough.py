# author:lee:2021/8/24 0024 13:53
'''
实现透传功能，保留原有接口的功能
原有的接口功能 http://127.0.0.1:5000
/login
/register
'''
import requests
from flask import make_response

def passThroughLo(data):
    '''
    判断条件：请求参数
    对登录的功能进行透传
    1.重新对原有的接口发起请求--获取响应
    2.构造响应make_response()
    3.返还响应
    :param data: 指的是前端收集到的请求参数
    :return:
    '''

    # 模拟发起请求
    url = 'http://127.0.0.1:5000/login'
    req = requests.post(url,json=data)

    # 构造响应
    resp = make_response(req.json())
    return resp


def passThroughRe(data):
    '''
    判断条件：请求参数
    对注册的功能进行透传
    1.重新对原有的接口发起请求--获取响应
    2.构造响应make_response()
    3.返还响应
    :param data: 指的是前端收集到的请求参数
    :return:
    '''

    # 模拟发起请求
    url = 'http://127.0.0.1:5000/register'
    req = requests.post(url,json=data)

    # 构造响应
    resp = make_response(req.json())
    return resp