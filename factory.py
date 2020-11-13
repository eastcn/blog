"""
@author: east
@date:
@function:
"""
from flask import Flask

from Utils.log import log
from config import CONFIG
from controller.Aticle import article
from controller.Movie import movie
from controller.Tools import tools
from controller.User import USER
from controller.sneakerlover import sneaker


def create_app():
    app = Flask('blog')
    app.config.from_object(CONFIG)
    log.info("注册各接口蓝本...")
    app.register_blueprint(article)
    app.register_blueprint(USER)
    app.register_blueprint(sneaker)
    app.register_blueprint(movie)
    app.register_blueprint(tools)
    log.info("注册成功...")
    return app
