# coding=utf-8
from flask import Flask, session
from flask import render_template
from datetime import timedelta
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import \
    CSRFProtect
from flask_qrcode import QRcode
from werkzeug.routing import BaseConverter

from sqlalchemy.orm import sessionmaker
from config import \
    SQLALCHEMY_DATABASE_URI_0, \
    WTF_CSRF_ENABLED, \
    UPLOADED_FILES_ALLOW, \
    SECRET_KEY, \
    UPLOADED_FILES_DEST,\
    SESSION_PERMANENT,\
    WTF_CSRF_TIME_LIMIT, \
    WTF_CSRF_SECRET_KEY

from flask_mistune import Mistune
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__, static_url_path='',
            static_folder="static",
            template_folder="templates")


class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


# ----------------------------------------------------------------------
app.config.from_object('config')

Session = sessionmaker()

# ----------------------------------------------------------------------
# configuration


app.url_map.converters['regex'] = RegexConverter
app.jinja_env.autoescape = True

app.config['UPLOADED_FILES_DEST'] = UPLOADED_FILES_DEST
app.config['UPLOADED_FILES_ALLOW'] = UPLOADED_FILES_ALLOW

app.config['SESSION_PERMANENT'] = SESSION_PERMANENT
app.config['PROPAGATE_EXCEPTIONS'] = True

app.config['WTF_CSRF_ENABLED'] = WTF_CSRF_ENABLED
app.config['WTF_CSRF_TIME_LIMIT'] = WTF_CSRF_TIME_LIMIT
app.config['WTF_CSRF_SECRET_KEY'] = WTF_CSRF_SECRET_KEY

# ----------------------------------------------------------------------

Session.configure(bind=SQLALCHEMY_DATABASE_URI_0)
# ----------------------------------------------------------------------
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
moment = Moment(app)
QRcode(app)
mail = Mail(app)
Mistune(app)
cors = CORS(app, resources={r"/api": {"origins": "http://localhost:5000"}})


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(days=365)


# ----------------------------------------------------------------------


@app.errorhandler(404)
def app_handle_404(e):
    return render_template('errors/404.html'), 404



# ----------------------------------------------------------------------
# routing

# all / landing / index
from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix='/main')
from .main import views

from .checkout import checkout as checkout_blueprint
app.register_blueprint(checkout_blueprint, url_prefix='/checkout')
from .checkout import views
# wallets
# xmr
from .wallet_xmr import wallet_xmr as wallet_xmr_blueprint
app.register_blueprint(wallet_xmr_blueprint, url_prefix='/xmr')

from .wallet_bch import wallet_bch as wallet_bch_blueprint
app.register_blueprint(wallet_bch_blueprint, url_prefix='/bch')



db.configure_mappers()
db.create_all()
db.session.commit()

