from flask_wtf import \
    FlaskForm
from wtforms import \
    StringField, \
    SubmitField,\
    SelectField
from wtforms.validators import DataRequired, Optional
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.classes.models import Country


class PackageFormUSPS(FlaskForm):
    # Basic info of package

    metric_or_imperial_form = StringField(validators=[DataRequired()])
    length = StringField(validators=[DataRequired()])

    width = StringField(validators=[DataRequired()])

    height = StringField(validators=[DataRequired()])

    weight_one = StringField(validators=[DataRequired()])
    weight_two = StringField(validators=[DataRequired()])

    signature_required = SelectField(u'Hour', choices=[('1', 'No Signature'),
                                                       ('2', 'Signature'),
                                                       ('3', 'Signature Required by Adult')])
    # From what address
    from_name_form = StringField(validators=[DataRequired()])

    from_street_address_form = StringField(validators=[DataRequired()])

    from_suitapt_form = StringField(validators=[Optional()])

    from_city_form = StringField(validators=[DataRequired()])

    from_state_form = StringField(validators=[DataRequired()])
    from_zip_form = StringField(validators=[DataRequired()])
    from_country_form = QuerySelectField(query_factory=lambda: Country.query.order_by(Country.name.asc()).all(),
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

    to_country_form = QuerySelectField(query_factory=lambda: Country.query.order_by(Country.name.asc()).all(),
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
