from app import db
from datetime import datetime


class XmrPrices(db.Model):
    __tablename__ = 'prices_monero'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class MoneroBlockHeight(db.Model):
    __tablename__ = 'monero_blockheight'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blockheight = db.Column(db.Integer)


class MoneroUnconfirmed(db.Model):
    __tablename__ = 'monero_unconfirmed'
    __bind_key__ = 'avengers'
    __table_args__ = {"schema": "avengers_wallet_monero", "useexisting": True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    unconfirmed1 = db.Column(db.DECIMAL(20, 12))
    txid1 = db.Column(db.TEXT)
