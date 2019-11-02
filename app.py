from flask import Flask
from factory import create_app

app = create_app()


# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run(port=8089)
