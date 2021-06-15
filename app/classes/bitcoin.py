from app import db



class BtcWalletAddresses(db.Model):
    __tablename__ = 'btc_wallet_addresses'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    btcaddress = db.Column(db.TEXT)
    status = db.Column(db.INTEGER)
