from app import db


class BtcPrices(db.Model):
    __tablename__ = 'prices_btc'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class BchPrices(db.Model):
    __tablename__ = 'prices_bch'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class XmrPrices(db.Model):
    __tablename__ = 'prices_monero'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class LtcPrices(db.Model):
    __tablename__ = 'prices_ltc'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price = db.Column(db.DECIMAL(50, 2))


class USPSShippingType(db.Model):
    __tablename__ = 'usps_shipping_selection'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shipment_name = db.Column(db.String(140))


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


class Tracking(db.Model):
    __tablename__ = 'tracking'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unique_id = db.Column(db.TEXT)
    last_seen = db.Column(db.TIMESTAMP())
    user_ip = db.Column(db.TEXT)
    user_agent = db.Column(db.TEXT)


class Transactions(db.Model):
    __tablename__ = 'transactions'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    blockheight = db.Column(db.INTEGER)
    address = db.Column(db.TEXT)
    txid = db.Column(db.TEXT)
    confirmations = db.Column(db.INTEGER)
    amount_btc = db.Column(db.DECIMAL(20, 8))
    amount_xmr = db.Column(db.DECIMAL(20, 8))
    amount_bch = db.Column(db.DECIMAL(20, 8))


# db.configure_mappers()
# db.create_all()
# db.session.commit()
