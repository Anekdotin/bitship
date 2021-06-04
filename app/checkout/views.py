from flask import \
    render_template, \
    redirect, \
    url_for, \
    flash, \
    request
import uuid
from decimal import Decimal
from datetime import datetime
from app import db, app

from app.main.forms import PackageFormUSPS, \
    CartForm,\
    SelectPaymentForm, \
    SelectShippingChoiceForm

from app.classes.models import User
from app.classes.shipping import ShippingChoices,\
    Orders,\
    OrderItem

from app.shipping_api.test import test_basic


@app.route('/', methods=['GET', 'POST'])
def checkout():
    # variables
    now = datetime.utcnow()

    # TODO GET CRYPTO PRICE OF EACH ORDERITEM AND ADD TO ORDER

    if request.method == 'GET':

        current_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        current_user_agent = request.headers.get('User-Agent')

        get_current_user = db.session \
            .query(User) \
            .filter(User.user_ip == current_ip, User.user_agent == current_user_agent) \
            .first()

        get_user_order_items = db.session \
            .query(OrderItem) \
            .filter(get_current_user.id == OrderItem.user_id) \
            .all()
        order = db.session \
            .query(Orders) \
            .filter(get_current_user.id == Orders.user_id) \
            .first()



        return render_template('checkout.html',
                               get_current_user=get_current_user,
                               order=order,
                               get_user_order_items=get_user_order_items)

    if request.method == 'POST':
        pass

