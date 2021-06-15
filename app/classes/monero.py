from app import db


class MoneroBlockHeight(db.Model):
    __tablename__ = 'monero_blockheight'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blockheight = db.Column(db.Integer)


class MoneroUnconfirmed(db.Model):
    __tablename__ = 'monero_unconfirmed'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer)
    unconfirmed1 = db.Column(db.DECIMAL(20, 12))
    txid1 = db.Column(db.TEXT)
