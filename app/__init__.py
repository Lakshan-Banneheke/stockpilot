from flask import Flask
from app.home import HOME_BP
APP = Flask(__name__)

APP.register_blueprint(HOME_BP, url_prefix='/')
