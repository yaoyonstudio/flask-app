from flask import Flask, jsonify
from model import db
from api import init_api
from common import Common

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
init_api(app)


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
