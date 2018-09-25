#!/usr/bin/env python
# -*- coding: utf-8 -*
'''
应用工厂方法(内部包括加载配置、初始化Flask扩展、注册蓝图等)
'''

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_restless import APIManager

db = SQLAlchemy()
migrate = Migrate()
api_restful = Api()
api_restless = APIManager()

def load_config(app):
    '''
    加载配置
    :param app:
    :return:
    '''

    # 加载默认配置(config/default.py)
    # 默认值，适用于所有的环境或交由具体环境进行覆盖
    # 举个例子，在config/default.py中设置DEBUG = False，在config/development.py中设置DEBUG = True
    app.config.from_object('config.default')

    # 从instance文件夹中加载配置(instance/config.py)
    # instance文件夹定义一些不能为人所知的配置变量，如数据库密码和API密钥等
    # 从config.py中分离出来是为了更好的维护私密信息
    app.config.from_pyfile('config.py')

    # 加载由环境变量APP_CONFIG_FILE指定的文件。这个环境变量的值应该是一个配置文件的绝对路径
    # 这个环境变量的设定方式取决于你运行你的应用的平台
    # 如果你是在一台标准的Linux服务器上运行，你可以使用一个shell脚本来设置环境变量并运行run.py
    # 如start.sh:
    #   APP_CONFIG_FILE=/var/www/yourapp/config/production.py
    #   python run.py
    app.config.from_envvar('APP_CONFIG_FILE', True)

    # 设置secret key
    app.secret_key = app.config['SECRET_KEY']


def initialize_extensions(app):
    '''
    初始化Flask扩展
    :param app:
    :return:
    '''
    db.init_app(app)
    migrate.init_app(app)
    api_restful.init_app(app)
    api_restless.init_app(app)



def register_blueprints(app):
    '''
    注册蓝图
    :param app:
    :return:
    '''

    from sample.hello import hello_blueprint
    app.register_blueprint(hello_blueprint)



def create_app():
    '''
    工厂方法创建Flask实例
    :return:
    '''

    # 实例化app
    app = Flask(__name__, instance_relative_config=True)

    # 加载配置 --> 初始化扩展 --> 注册蓝图
    load_config(app)
    initialize_extensions(app)
    register_blueprints(app)

    # 用flask-script的manager替换Flask的app
    manager = Manager(app)

    manager.add_command('db', MigrateCommand)

    return manager
