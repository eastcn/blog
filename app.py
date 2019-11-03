from flask import Flask
from flask_cors import CORS
from factory import create_app

app = create_app()

@app.route('/hello')
def hello():
    return "hello"

if __name__ == '__main__':
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.run(port=8089)
