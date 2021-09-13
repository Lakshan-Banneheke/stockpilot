from flask import Flask
from app.home import HOME_BP
from flask_cors import CORS

APP = Flask(__name__)
CORS(APP)

APP.register_blueprint(HOME_BP, url_prefix='/')
