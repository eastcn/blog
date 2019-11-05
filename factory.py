"""
@author: east
@date:
@function:
"""
from flask import Flask
from controller.Aticle import article
from controller.User import USER
from controller.sneakerlover import sneaker
from config import CONFIG


def create_app():
    app = Flask('blog')
    app.config.from_object(CONFIG)
    app.register_blueprint(article)
    app.register_blueprint(USER)
    app.register_blueprint(sneaker)
    return app