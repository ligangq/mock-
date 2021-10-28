
from flask import Flask, jsonify
import tool
from flask import request
'''
1.实现登录和注册
接口文档
接口名字      method   url                              参数
登录接口      post     http://127.0.0.1:5000/login       {"name":"yaoyao","password": "yaoyao"}
注册接口      post     http://127.0.0.1:5000/register    {"name":"yaoyao","password": "yaoyao"}
2.没有页面，只有接口

'''
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/login', methods=['POST'])
def login():
    '''
    登录接口
    :return:
    '''
    data = request.get_json()

    if 'name' not in data or not data['name']:
        return jsonify(
            {'data': data,
             'message': '无效的参数:name',
             'code': 404})
    if 'password' not in data or not data['password']:
        return jsonify(
            {'data': data,
             'message': '无效的参数:password',
             'code': 404})

    name = data['name']
    password = data['password']
    try:
        if tool.read_open(name, password):
            return jsonify({'data': data, 'message': '登陆成功', 'code': 200})

        else:
            return jsonify({'data': data, 'message': '用户不存在或密码错误', 'code': 401})
    except Exception as e:
        return jsonify({'data': data, 'message': "未知异常", 'code': 500})


@app.route('/register', methods=['POST'])
def register():
    '''
    注册接口
    :return:
    '''
    data = request.get_json()
    if 'name' not in data or not data['name']:
        return jsonify(
            {'data': data,
             'message': '无效的参数:name',
             'code': 404})
    if 'password' not in data or not data['password']:
        return jsonify(
            {'data': data,
             'message': '无效的参数:password',
             'code': 404})

    name = data['name']
    password = data['password']

    try:
        tool.write_csv(name, password)
        return jsonify({'data': data, 'message': '注册成功', 'code': 200})

    except Exception as e:
        return jsonify({'data': data, 'message': e, 'code':204})


if __name__ == '__main__':
    app.run(debug=True,port=1235)