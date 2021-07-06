from app import db


class ShippingLabels(db.Model):
    __tablename__ = 'labels'
    __bind_key__ = 'shipbit'
    __table_args__ = {"schema": "public"}

    id = db.Column(db.Integer, primary_key=True)
    # get current user ip
    user_id = db.Column(db.Integer)
    # time order was created
    creation_time = db.Column(db.TEXT)

    label_url = db.Column(db.TEXT)
    messages = db.Column(db.TEXT)
    metadata_order = db.Column(db.TEXT)
    object_created = db.Column(db.TEXT)
    object_id = db.Column(db.TEXT)
    object_owner = db.Column(db.TEXT)
    object_state = db.Column(db.TEXT)
    object_updated = db.Column(db.TEXT)
    order = db.Column(db.TEXT)
    parcel = db.Column(db.TEXT)
    rate = db.Column(db.TEXT)
    status = db.Column(db.TEXT)
    tracking_number = db.Column(db.TEXT)
    tracking_status = db.Column(db.TEXT)
    tracking_url_provider = db.Column(db.TEXT)
