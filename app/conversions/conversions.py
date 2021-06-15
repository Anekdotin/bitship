from app import app, db
from decimal import Decimal
from app.classes.models import BtcPrices, BchPrices, XmrPrices


def floating_decimals(f_val, dec):
    prc = "{:."+str(dec)+"f}"
    return Decimal(prc.format(f_val))


# BITCOIN
def btc_crypto_to_local(amount):
    # convert monero amount to local
    getcurrentprice = db.session.query(BtcPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(bt) * Decimal(amount)
    c = floating_decimals(z, 2)
    return c


def btc_local_to_crypto(amount):
    # convert local to bitcoin cash
    getcurrentprice = db.session.query(BtcPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(amount) / Decimal(bt)
    c = floating_decimals(z, 8)
    return c

# BITCOIN CASH
def bch_crypto_to_local(amount):
    # convert bitcoin amount to local
    getcurrentprice = db.session.query(BchPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(bt) * Decimal(amount)
    c = floating_decimals(z, 2)
    return c


def bch_local_to_crypto(amount):
    # convert local to bitcoin cash
    getcurrentprice = db.session.query(BchPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(amount) / Decimal(bt)
    c = floating_decimals(z, 8)
    return c


# MONERO
def xmr_crypto_to_local(amount):
    # convert bitcoin cash amount to local
    getcurrentprice = db.session.query(XmrPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(bt) * Decimal(amount)
    c = floating_decimals(z, 2)
    return c


def xmr_local_to_crypto(amount):
    # convert local to bitcoin cash
    getcurrentprice = db.session.query(XmrPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(amount) / Decimal(bt)
    c = floating_decimals(z, 8)
    return c


