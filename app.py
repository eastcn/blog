from flask_cors import CORS

from factory import create_app

app = create_app()
CORS(app, origins="*", supports_credentials=True)


@app.route('/hello')
def hello():
    return "hello"


if __name__ == '__main__':
    app.run(port=8089)
