from flask_wtf import \
    FlaskForm
from wtforms import \
    StringField, \
    SubmitField, \
    SelectField
from wtforms.validators import DataRequired, Optional
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.classes.models import Country


class PackageFormUSPS(FlaskForm):
    # Basic info of package
    metric_or_imperial_form = StringField(validators=[DataRequired()])

    shipping_type = SelectField(u'Select Shipping', choices=[
        ('1', 'Select a flate Rate Package'),
        ('7', 'letter'),
        ('8', 'Flat Rate Envolope Letter'),
        ('9', 'Flat Rate Envolope Legal'),
        ('10', 'Flat Rate Envolope Padded'),
        ('11', 'Flat Rate Envolope Small'),
        ('12', 'Flat Rate Envolope Window'),
        ('13', 'Flat Rate Envolope Gift Card'),
        ('14', 'Flat Rate Envolope CardBoard'),
        ('15', 'Flat Rate Box Small'),
        ('16', 'Flat Rate Box Medium'),
        ('17', 'Flat Rate Box Large'),
        ('18', 'Flat Rate Box Large Board Game'),
    ])

    length = StringField(validators=[Optional()])
    width = StringField(validators=[Optional()])
    height = StringField(validators=[Optional()])
    weight_one = StringField(validators=[Optional()])
    weight_two = StringField(validators=[Optional()])

    signature_required = SelectField(u'Signature', choices=[('1', 'No Signature'),
                                                       ('2', 'Signature'),
                                                       ('3', 'Signature Required by Adult')])
    # From what address
    from_name_form = StringField(validators=[DataRequired()])

    from_street_address_form = StringField(validators=[DataRequired()])

    from_suitapt_form = StringField(validators=[Optional()])

    from_city_form = StringField(validators=[DataRequired()])

    from_state_form = StringField(validators=[DataRequired()])
    from_zip_form = StringField(validators=[DataRequired()])
    from_country_form = QuerySelectField(query_factory=lambda: Country.query.order_by(Country.id.asc()).all(),
                                         get_label='name',
                                         validators=[
                                             DataRequired()
                                         ])
    from_phone_form = StringField(validators=[Optional()])

    # To what address
    to_name_form = StringField(validators=[DataRequired()])

    to_street_address_form = StringField(validators=[DataRequired()])

    to_suitapt_form = StringField(validators=[Optional()])
    to_zip_form = StringField(validators=[DataRequired()])

    to_city_form = StringField(validators=[DataRequired()])

    to_state_form = StringField(validators=[DataRequired()])

    to_country_form = QuerySelectField(query_factory=lambda: Country.query.order_by(Country.id.asc()).all(),
                                       get_label='name',
                                       validators=[
                                           DataRequired()
                                       ])
    to_phone_form = StringField(validators=[Optional()])

    package_submit_form = SubmitField('')

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self, *args, **kwargs):

        rv = FlaskForm.validate(self)

        if rv:
            return True
        else:
            return False


class CartForm(FlaskForm):
    # Basic info of package

    delete_form = SubmitField('')

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)

    def validate(self, *args, **kwargs):

        rv = FlaskForm.validate(self)

        if rv:
            return True
        else:
            return False


class SelectPaymentForm(FlaskForm):
    submit = SubmitField('')


class SelectShippingChoiceForm(FlaskForm):

    submit = SubmitField('')


class TrackingForm(FlaskForm):
    submit = SubmitField('')


class LostOrderForm(FlaskForm):
    submit = SubmitField('')
