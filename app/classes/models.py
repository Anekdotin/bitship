from app import db
from datetime import datetime



class Country(db.Model):
    __tablename__ = 'countries'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ab = db.Column(db.TEXT)
    name = db.Column(db.TEXT)
    numericcode = db.Column(db.INTEGER)


class User(db.Model):
    __tablename__ = 'user'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unique_id = db.Column(db.TEXT)
    last_seen = db.Column(db.TIMESTAMP())
    user_ip = db.Column(db.TEXT)
    user_agent = db.Column(db.TEXT)


db.create_all()
db.session.commit()
