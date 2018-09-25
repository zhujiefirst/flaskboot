#!/usr/bin/env python
# -*- coding: utf-8 -*
'''
蓝图 hello 模块初始化
'''

from flask import Blueprint

hello_blueprint = Blueprint('hello', __name__, url_prefix='/hello')

from . import routers