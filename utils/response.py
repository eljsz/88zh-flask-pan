# -*- coding: utf-8 -*-
# @Time    : 2024/1/6
# @Author  : lhq
# @File    : response.py
# @Description :

from flask import jsonify, make_response
from functools import wraps

def response_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        response = f(*args, **kwargs)
        if isinstance(response, tuple):
            status_code, data = response
            return make_response(jsonify({'data': data}), status_code)
        else:
            return jsonify({'status_code': 200, 'data': response})
    return wrapper
