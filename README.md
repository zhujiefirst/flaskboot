# FlaskBoot

快速搭建基于Flask的项目雏形。

# 我们有什么

## Flask扩展

FlaskBoot初始化时自带以下Flask扩展：

1. [flask-script](https://flask-script.readthedocs.io/en/latest/)
2. [flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/)
3. [flask-migrate](https://flask-migrate.readthedocs.io/en/latest/)
4. [flask-restful](https://flask-restful.readthedocs.io/en/latest/)
5. [flask-restless](https://flask-restless.readthedocs.io/)

## 应用工厂
参见方法*create_app*.

## 环境配置
提供不同环境配置文件，*default.py*提供默认基础配置，*development.py*、*production.py*、*staging.py*分别提供开发环境、生产环境、演示/模拟环境配置。

## 蓝图方式划分模块
*sample*下，以蓝图区分模块。蓝图注册在*sample/__init__.py*中。

