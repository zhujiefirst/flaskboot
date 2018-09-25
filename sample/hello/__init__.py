from flask import Blueprint

hello_blueprint = Blueprint('hello', __name__, url_prefix='/hello')

from . import routers