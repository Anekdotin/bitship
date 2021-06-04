from app import app, db
from decimal import Decimal
from app.classes.monero import XmrPrices
from app.classes.bitcoin import BtcPrices
from app.classes.bitcoin_cash import BchPrices


def floating_decimals(f_val, dec):
    prc = "{:."+str(dec)+"f}"
    return Decimal(prc.format(f_val))


# BITCOIN
def xmr_converttolocal(amount):
    # convert monero amount to local
    getcurrentprice = db.session.query(BtcPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(bt) * Decimal(amount)
    c = floating_decimals(z, 2)
    return c


def xmr_convertlocaltobtc(amount):
    # convert local to bitcoin cash
    getcurrentprice = db.session.query(BtcPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(amount) / Decimal(bt)
    c = floating_decimals(z, 8)
    return c

# BITCOIN CASH
def btc_converttolocal(amount):
    # convert bitcoin amount to local
    getcurrentprice = db.session.query(BchPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(bt) * Decimal(amount)
    c = floating_decimals(z, 2)
    return c


def btc_convertlocaltobtc(amount):
    # convert local to bitcoin cash
    getcurrentprice = db.session.query(BchPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(amount) / Decimal(bt)
    c = floating_decimals(z, 8)
    return c


# MONERO
def btc_cash_converttolocal(amount):
    # convert bitcoin cash amount to local
    getcurrentprice = db.session.query(XmrPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(bt) * Decimal(amount)
    c = floating_decimals(z, 2)
    return c


def btc_cash_convertlocaltobtc(amount):
    # convert local to bitcoin cash
    getcurrentprice = db.session.query(XmrPrices).get(1)
    bt = getcurrentprice.price
    z = Decimal(amount) / Decimal(bt)
    c = floating_decimals(z, 8)
    return c


