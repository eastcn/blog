from flask import Flask
from flask_cors import CORS
from factory import create_app

app = create_app()

@app.route('/hello')
def hello():
    return "hello"

if __name__ == '__main__':
    CORS(app,supports_credentials=True)
    app.run(port=8089)
