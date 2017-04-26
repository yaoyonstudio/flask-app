from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)

    db.init_app(app)

    # 用户模块
    from app.users.api import init_api
    init_api(app)

    # 新闻模块
    from app.news.api import init_api
    init_api(app)

    return app
