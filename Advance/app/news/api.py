from flask import jsonify, request
from app.news.model import News
from app.common import Common

def init_api(app):
    @app.route('/news')
    def news():
        return jsonify(Common.trueReturn(Common, '这是新闻模块', "提示信息"))
