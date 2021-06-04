from app import db
from datetime import datetime


class BchPrices(db.Model):
    __tablename__ = 'prices_bch'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))
