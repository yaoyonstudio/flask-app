from flask_sqlalchemy import SQLAlchemy

from app import db

class News(db.Model):
    news_id = db.Column(db.Integer, primary_key=True)
    news_title = db.Column(db.String(60), nullable=False)
    news_desc = db.Column(db.String(30), nullable=False)
    news_date = db.Column(db.DateTime)
    news_content = db.Column(db.Text, nullable=False)
