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
def index():
    # variables
    now = datetime.utcnow()

    # forms
    package_basics = PackageFormUSPS()
    cartform = CartForm()
    shipchoiceform = SelectShippingChoiceForm()

    # Get User
    current_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    current_user_agent = request.headers.get('User-Agent')
    get_current_user = db.session \
        .query(User) \
        .filter(User.user_ip == current_ip, User.user_agent == current_user_agent) \
        .first()

    # list of rates
    rates_list = []

    # need to see if there is a shipment..if not get it

    if request.method == 'GET':

        if get_current_user is not None:
            # see if user has an order
            get_user_order = db.session \
                .query(Orders) \
                .filter(get_current_user.id == Orders.user_id) \
                .first()

            # get users selected items
            get_user_listed_items = db.session \
                .query(OrderItem) \
                .filter(get_current_user.id == OrderItem.user_id) \
                .all()

            # get users selected items
            user_choices_shipping = db.session \
                .query(ShippingChoices) \
                .filter(get_current_user.id == ShippingChoices.owner_user_id) \
                .order_by(ShippingChoices.estimated_days.asc()) \
                .all()

            latest_shipping_choice = db.session \
                .query(ShippingChoices) \
                .filter(get_current_user.id == ShippingChoices.owner_user_id) \
                .order_by(ShippingChoices.object_created.desc()) \
                .first()


        else:
            get_user_listed_items = None
            get_user_order = None
            user_choices_shipping = None
            latest_shipping_choice = None

        return render_template('index.html',
                               latest_shipping_choice=latest_shipping_choice,
                               package_basics=package_basics,
                               shipchoiceform=shipchoiceform,
                               cartform=cartform,
                               get_user_listed_items=get_user_listed_items,
                               get_user_order=get_user_order,
                               user_choices_shipping=user_choices_shipping
                               )

    if request.method == 'POST':

        if package_basics.package_submit_form.data:
            print("@!1")
            # form data basics
            f_country = package_basics.from_country_form.data
            from_country = f_country.ab

            t_country = package_basics.to_country_form.data
            to_country = t_country.ab

            # set as default usps right now..change later
            type_of_shipping = 1
            # what service was selected
            if type_of_shipping == 1:
                shipping_service_selected = 'USPS'
            elif type_of_shipping == 2:
                shipping_service_selected = 'UPS'
            else:
                shipping_service_selected = 'FEDEX'

            # create a current user if we cant find one
            if get_current_user is None:
                new_user_id = str(uuid.uuid4())
                new_user = User(
                    unique_id=new_user_id,
                    last_seen=now,
                    user_ip=current_ip,
                    user_agent=current_user_agent
                )
                db.session.add(new_user)
                db.session.commit()
            else:
                get_current_user = db.session \
                    .query(User) \
                    .filter(User.user_ip == current_ip,
                            User.user_agent == current_user_agent) \
                    .first()

            # see if order exists if not create it
            get_user_order = db.session \
                .query(Orders) \
                .filter(get_current_user.id == Orders.user_id) \
                .first()
            if get_user_order is None:
                neworder = Orders(
                    creation_time=now,
                    user_id=get_current_user.id,
                    total_cost_btc=0,
                    total_cost_bch=0,
                    total_cost_xmr=0,
                    total_cost_usd=0,
                )
                db.session.add(neworder)
                db.session.commit()
                neworder = db.session \
                    .query(Orders) \
                    .filter(get_current_user.id == Orders.user_id) \
                    .first()
            else:
                neworder = db.session \
                    .query(Orders) \
                    .filter(get_current_user.id == Orders.user_id) \
                    .first()

            #  Call the USPS Functions
            #  function returns  shipping info
            shipment_data = test_basic.get_rates_usps(
                from_name=package_basics.from_name_form.data,
                from_address_1=package_basics.from_street_address_form.data,
                from_address_2=package_basics.from_suitapt_form.data,
                from_city=package_basics.from_city_form.data,
                from_state=package_basics.from_state_form.data,
                from_zip=package_basics.from_zip_form.data,
                from_country=from_country,
                from_phone=package_basics.from_phone_form.data,

                to_name=package_basics.to_name_form.data,
                to_address_1=package_basics.to_street_address_form.data,
                to_address_2=package_basics.to_suitapt_form.data,
                to_city=package_basics.to_city_form.data,
                to_state=package_basics.to_state_form.data,
                to_zip=package_basics.to_zip_form.data,
                to_country=to_country,
                to_phone=package_basics.from_phone_form.data,

                mass_unit_type=package_basics.from_name_form.data,
                unit_length=package_basics.length.data,
                unit_width=package_basics.width.data,
                unit_height=package_basics.height.data,

                unit_weight=package_basics.weight_one.data,
            )

            # location # grab data from parcel respons so we know its accurate
            location = shipment_data.parcels
            location_height = location[0]['height']
            location_length = location[0]['length']
            location_mass_unit = location[0]['mass_unit']
            location_weight = location[0]['weight']
            location_width = location[0]['width']

            # rates
            rates_func = shipment_data.rates
            for f in rates_func:
                y = [
                    # 0
                    f['object_id'],
                    # 1
                    f['shipment'],
                    # 2
                    f['duration_terms'],
                    # 3
                    f['amount'],
                    # 4
                    f['currency'],
                    # 5
                    f['currency'],
                    # 6
                    f['duration_terms'],
                    # 7
                    f['estimated_days'],
                    # 8
                    f['carrier_account'],
                    # 9
                    f['provider'],
                    # 10
                    f['servicelevel']['name'],
                    # 11
                    f['servicelevel']['token'],
                ]

                rates_list.append(y)
            # put info into database
            # put into the database the shipping rates
            for f in rates_list:
                print(f)

                # calculate a 1$ profit for each label
                shipment_cost = Decimal(f[3])

                profit = Decimal(shipment_cost) + Decimal(1.00)

                shipment_selection = ShippingChoices(
                    object_created=now,
                    owner_user_id=get_current_user.id,
                    object_id=f[0],
                    shipment=f[1],
                    currency=f[5],
                    duration_terms=f[6],
                    estimated_days=f[7],
                    carrier_account=f[8],
                    provider=f[9],
                    name=f[10],
                    token=f[11],
                    price_before_profit=str(shipment_cost),
                    price_after_profit=profit,
                    currency_local="USD",
                    distance_unit=1,

                    height=location_height,
                    length=location_length,
                    mass_unit=location_mass_unit,
                    weight=location_weight,
                    width=location_width,

                    from_name=package_basics.from_name_form.data,
                    from_street_address=package_basics.from_street_address_form.data,
                    from_apt_suite=package_basics.from_suitapt_form.data,
                    from_city=package_basics.from_city_form.data,
                    from_state=package_basics.from_state_form.data,
                    from_zip=package_basics.from_zip_form.data,
                    from_country=from_country,
                    from_phone_number=package_basics.from_phone_form.data,

                    to_name=package_basics.to_name_form.data,
                    to_street_address=package_basics.to_street_address_form.data,
                    to_apt_suite=package_basics.to_suitapt_form.data,
                    to_city=package_basics.to_city_form.data,
                    to_state=package_basics.to_state_form.data,
                    to_zip=package_basics.to_zip_form.data,
                    to_country=to_country,
                    to_phone_number=package_basics.from_phone_form.data,



                )

                db.session.add(shipment_selection)

            # need to signal to jinja for popup that there is a shipping selection
            neworder.new_selection = 1

            db.session.add(neworder)
            db.session.commit()

            return redirect(url_for('index'))

        if shipchoiceform.submit.data:

            data = request.form['selectpayment']

            print(data)
            get_user_order = db.session \
                .query(Orders) \
                .filter(get_current_user.id == Orders.user_id) \
                .first()

            # get selected shipping choice
            get_the_shipping_choice = db.session \
                .query(ShippingChoices) \
                .filter(ShippingChoices.object_id == data) \
                .first()

            if get_the_shipping_choice.provider == 'USPS':
                type_of_shipping = 1
            elif get_the_shipping_choice.provider == 'UPS':
                type_of_shipping = 2
            else:
                type_of_shipping = 3

            # add the shipment choice as an item
            # create a new order item
            new_shipment = OrderItem(
                main_shipment_id=get_the_shipping_choice.shipment,
                object_id_selected_order=get_the_shipping_choice.object_id,

                # Main Order Selection
                user_id=get_current_user.id,
                order_id=get_user_order.id,
                type_of_package=1,
                type_of_package_name=get_the_shipping_choice.name,
                service=type_of_shipping,
                metric_or_imperial=1,

                length_of_package=get_the_shipping_choice.length,
                width_of_package=get_the_shipping_choice.width,
                height_of_package=get_the_shipping_choice.height,
                weight_one=get_the_shipping_choice.height,
                weight_two=get_the_shipping_choice.length,

                from_name=get_the_shipping_choice.from_name,
                from_street_address=get_the_shipping_choice.from_street_address,
                from_apt_suite=get_the_shipping_choice.from_apt_suite,
                from_city=get_the_shipping_choice.from_city,
                from_state=get_the_shipping_choice.from_state,
                from_zip=get_the_shipping_choice.from_zip,
                from_country=get_the_shipping_choice.from_country,
                from_phone_number=get_the_shipping_choice.from_phone_number,

                to_name=get_the_shipping_choice.to_name,
                to_street_address=get_the_shipping_choice.to_street_address,
                to_apt_suite=get_the_shipping_choice.to_apt_suite,
                to_city=get_the_shipping_choice.to_city,
                to_state=get_the_shipping_choice.to_state,
                to_zip=get_the_shipping_choice.to_zip,
                to_country=get_the_shipping_choice.to_country,
                to_phone_number=get_the_shipping_choice.to_phone_number,

                cost_usd=get_the_shipping_choice.price_before_profit,
                cost_btc=0,
                cost_bch=0,
                cost_xmr=0,

            )

            db.session.add(new_shipment)

            # finally delete all the shipping choices
            get_the_shipping_choices = db.session \
                .query(ShippingChoices) \
                .filter(get_current_user.id == ShippingChoices.owner_user_id) \
                .all()

            for choice in get_the_shipping_choices:
                db.session.delete(choice)

            get_user_order.new_selection = 0

            # commit to the database
            db.session.commit()

            # return user back to index
            return redirect(url_for('index'))

        else:
            return redirect(url_for('index'))


@app.route('/selectpayment', methods=['GET', 'POST'])
def second_page():

    payment_form = SelectPaymentForm()
    # see if a new user
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

    if request.method == 'GET':

        return render_template('second_page.html',
                               get_user_order_items=get_user_order_items,
                               payment_form=payment_form)

    if request.method == 'POST':
        data = request.form['whatcoin']
        if data == '1':
            payment_order_type = 1
        elif data == '2':
            payment_order_type = 2
        elif data == '3':
            payment_order_type = 3
        else:
            payment_order_type = 0

        order.order_payment_type = payment_order_type

        db.session.add(order)
        db.session.commit()

        return redirect(url_for('third_page'))


@app.route('/confirmorder', methods=['GET'])
def third_page():

    ##TODO GET CRYPTO PRICE OF EACH ORDERITEM AND ADD TO ORDER

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

        return render_template('third_page.html',
                               get_current_user=get_current_user,
                               order=order,
                               get_user_order_items=get_user_order_items)

    if request.method == 'POST':
        pass


@ app.route('/deleteorder/<int:order_id>', methods=['GET', 'POST'])
def delete_order(order_id):
    if request.method == 'GET':

        the_item = db.session \
            .query(OrderItem) \
            .filter(OrderItem.id == order_id) \
            .first()

        db.session.delete(the_item)
        db.session.commit()
        flash("Order Deleted", category="danger")
        return redirect(url_for('index'))


@app.route('/tracking', methods=['GET'])
def tracking():
    if request.method == 'GET':

        return render_template('main/tracking.html')

    if request.method == 'POST':
        pass


@app.route('/cart', methods=['GET'])
def view_cart():
    if request.method == 'GET':

        return render_template('main/cart.html')

    if request.method == 'POST':
        pass


@app.route('/csv', methods=['GET'])
def upload_csv():
    if request.method == 'GET':

        return render_template('main/csv.html')

    if request.method == 'POST':
        pass


@app.route('/cart', methods=['GET'])
def faq():
    if request.method == 'GET':

        return render_template('main/faq.html')

    if request.method == 'POST':
        pass


@app.route('/internationalhelp', methods=['GET'])
def international_help():
    if request.method == 'GET':

        return render_template('main/internationalhelp.html')

    if request.method == 'POST':
        pass


@app.route('/usahelp', methods=['GET'])
def usa_help():
    if request.method == 'GET':

        return render_template('main/usahelp.html')

    if request.method == 'POST':
        pass
