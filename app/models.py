from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from app import db

Base = declarative_base()


class Like(db.Model):
    __tablename__ = 'likes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    content_id = db.Column(db.Integer)
