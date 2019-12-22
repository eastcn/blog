"""
@author: east
@date:
@function:
"""
from flask import Flask
from controller.Aticle import article
from controller.User import USER
from controller.sneakerlover import sneaker
from controller.Movie import movie
from config import CONFIG
from Utils.log import log


def create_app():
    app = Flask('blog')
    app.config.from_object(CONFIG)
    log.info("注册各接口蓝本...")
    app.register_blueprint(article)
    app.register_blueprint(USER)
    app.register_blueprint(sneaker)
    app.register_blueprint(movie)
    log.info("注册成功...")
    return app
