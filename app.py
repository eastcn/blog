from flask import Flask
from factory import create_app

app = create_app()

@app.route('/hello')
def hello():
    return "hello"

if __name__ == '__main__':
    app.run(port=8089)
