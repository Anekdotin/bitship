from app import db


class Orders(db.Model):
    __tablename__ = 'orders'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True)
    # get current user ip
    user_id = db.Column(db.Integer)
    order_code = db.Column(db.String(140))
    # time order was created
    creation_time = db.Column(db.TIMESTAMP())

    # cost in crypto
    total_cost_btc = db.Column(db.DECIMAL(20, 8))
    total_cost_bch = db.Column(db.DECIMAL(20, 8))
    total_cost_xmr = db.Column(db.DECIMAL(20, 8))
    # cost in usd
    total_cost_usd = db.Column(db.DECIMAL(20, 2))

    # which coin using
    order_payment_type = db.Column(db.Integer)
    # shows if there is a shipping selection
    new_selection = db.Column(db.Integer)

    status = db.Column(db.Integer)


class OrderItem(db.Model):
    __tablename__ = 'orderitems'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)
    # the main order
    main_shipment_id = db.Column(db.String(140))
    # the specific item selected from the order
    object_id_selected_order = db.Column(db.String(140))

    order_id = db.Column(db.Integer)
    # Main Order Selection
    service = db.Column(db.Integer)
    metric_or_imperial = db.Column(db.Integer)

    # size and weight
    type_of_package = db.Column(db.Integer)
    type_of_package_name = db.Column(db.TEXT)
    length_of_package = db.Column(db.DECIMAL(10, 4))
    width_of_package = db.Column(db.DECIMAL(10, 4))
    height_of_package = db.Column(db.DECIMAL(10, 4))
    weight_one = db.Column(db.DECIMAL(10, 4))
    weight_two = db.Column(db.DECIMAL(10, 4))

    # FROM
    from_name = db.Column(db.TEXT)
    from_street_address = db.Column(db.TEXT)
    from_apt_suite = db.Column(db.TEXT)
    from_city = db.Column(db.TEXT)
    from_state = db.Column(db.String(140))
    from_zip = db.Column(db.String(140))
    from_country = db.Column(db.String(140))
    from_phone_number = db.Column(db.String(140))

    # TO
    to_name = db.Column(db.TEXT)
    to_street_address = db.Column(db.TEXT)
    to_apt_suite = db.Column(db.TEXT)
    to_city = db.Column(db.String(140))
    to_state = db.Column(db.String(140))
    to_zip = db.Column(db.String(140))
    to_country = db.Column(db.String(140))
    to_phone_number = db.Column(db.String(140))

    # options
    signature_required = db.Column(db.Integer)

    cost_btc = db.Column(db.DECIMAL(20, 8))
    cost_bch = db.Column(db.DECIMAL(20, 8))
    cost_xmr = db.Column(db.DECIMAL(20, 8))
    cost_usd = db.Column(db.DECIMAL(20, 2))

    order_status = db.Column(db.String(140))

    token = db.Column(db.String(140))
    carrier_account = db.Column(db.String(140))

    address_status = db.Column(db.String(140))
    address_message = db.Column(db.TEXT)


class ShippingChoices(db.Model):
    __tablename__ = 'shipping_choices_selector'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # created
    object_created = db.Column(db.TIMESTAMP())
    # users id
    owner_user_id = db.Column(db.Integer)
    # main order id
    order_id = db.Column(db.Integer)
    # object id
    object_id = db.Column(db.String(140))
    # shipment id
    shipment = db.Column(db.String(140))
    # price in database
    price_before_profit = db.Column(db.DECIMAL(10, 2))
    # price to show customer
    price_after_profit = db.Column(db.DECIMAL(10, 2))
    # currency ie USD CAD EUR
    currency = db.Column(db.String(140))
    # cost local to website
    currency_local = db.Column(db.String(140))

    # shipping estimate
    duration_terms = db.Column(db.String(140))
    estimated_days = db.Column(db.String(140))

    # id of carrier account
    carrier_account = db.Column(db.String(140))
    # name of shipper
    provider = db.Column(db.String(140))
    # shipper name of service
    name = db.Column(db.String(140))
    # token for service
    token = db.Column(db.String(140))

    # package sizing
    distance_unit = db.Column(db.String(140))
    height = db.Column(db.String(140))
    length = db.Column(db.String(140))
    mass_unit = db.Column(db.String(140))
    weight = db.Column(db.String(140))
    width = db.Column(db.String(140))

    # size and weight
    type_of_package = db.Column(db.Integer)
    type_of_package_name = db.Column(db.TEXT)
    length_of_package = db.Column(db.DECIMAL(10, 4))
    width_of_package = db.Column(db.DECIMAL(10, 4))
    height_of_package = db.Column(db.DECIMAL(10, 4))
    weight_one = db.Column(db.DECIMAL(10, 4))
    weight_two = db.Column(db.DECIMAL(10, 4))

    # FROM
    from_name = db.Column(db.TEXT)
    from_street_address = db.Column(db.TEXT)
    from_apt_suite = db.Column(db.TEXT)
    from_city = db.Column(db.TEXT)
    from_state = db.Column(db.String(140))
    from_zip = db.Column(db.String(140))
    from_country = db.Column(db.String(140))
    from_phone_number = db.Column(db.String(140))

    # TO
    to_name = db.Column(db.TEXT)
    to_street_address = db.Column(db.TEXT)
    to_apt_suite = db.Column(db.TEXT)
    to_city = db.Column(db.TEXT)
    to_state = db.Column(db.String(140))
    to_zip = db.Column(db.String(140))
    to_country = db.Column(db.String(140))
    to_phone_number = db.Column(db.String(140))

    # options
    signature_required = db.Column(db.Integer)
#
# #
# db.configure_mappers()
# db.create_all()
# db.session.commit()
