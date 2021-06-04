from app import db
from datetime import datetime


class BtcPrices(db.Model):
    __tablename__ = 'prices_btc'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class BtcWalletAddresses(db.Model):
    __tablename__ = 'btc_wallet_addresses'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btcaddress = db.Column(db.TEXT)
    status = db.Column(db.INTEGER)
