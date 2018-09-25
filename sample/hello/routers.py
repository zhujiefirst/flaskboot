#!/usr/bin/env python
# -*- coding: utf-8 -*
'''
蓝图 hello 路由
'''

from . import hello_blueprint
from flask import jsonify

@hello_blueprint.route('/')
def index():
    return jsonify(rsp='hello world!')

@hello_blueprint.route('/<user>')
def hello_user(user):
    return jsonify(rsp='hello {}!'.format(user))
