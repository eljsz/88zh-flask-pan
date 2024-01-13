# -*- coding: utf-8 -*-
# @Time    : 2024/1/4
# @Author  : lhq
# @File    : app.py
# @Description :
import json

import redis
from flask import Flask, request
from flask_cors import CORS

from resource.alypw import alypw
from resource.leijing import leijing
from resource.pan666 import pan666
from resource.wordpress import wordpress
from resource.yunpan1 import yunpan1
from resource.yunpanziyuan import yunpanziyuan
from utils.response import response_decorator

app = Flask(__name__)
CORS(app)

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


@app.route('/api/tabs_list', methods=['GET'])
@response_decorator
def tabs_list():
    return [
        '云盘分享网&alypw',
        '盘66&pan666',
        '阿里云盘&wordpress',
        '云盘1&yunpan1',
        '雷鲸(天翼云)&leijing',
        '云盘资源&yunpanziyuan'
    ]


@app.route('/api/get_list', methods=['GET'])
@response_decorator
def get_list():
    keyword = request.args.get('keyword')
    active_name = request.args.get('activeName')
    r_keyword = keyword + active_name
    result = [{'title': '没有找到内容', 'url': 'https://www.baidu.com'},
              {'title': '没有找到内容', 'url': 'https://www.baidu.com'}]
    if keyword is None:
        return result

    # 获取键的值
    r_data = r.get(r_keyword)
    if r_data is not None:
        return json.loads(r_data)

    if active_name == 'alypw':
        result = alypw(keyword)
    elif active_name == 'pan666':
        result = pan666(keyword)
    elif active_name == 'wordpress':
        result = wordpress(keyword)
    elif active_name == 'yunpan1':
        result = yunpan1(keyword)
    elif active_name == 'leijing':
        result = leijing(keyword)
    elif active_name == 'yunpanziyuan':
        result = yunpanziyuan(keyword)

    r.set(r_keyword, json.dumps(result))
    # 过期时间 4个小时
    r.expire(r_keyword, 14400)

    return result


if __name__ == '__main__':
    app.run(debug=True)
