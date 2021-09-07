from flask import Flask
from app.home import HOME_BP
from app.binanceStream import BINANCE_BP

APP = Flask(__name__)

APP.register_blueprint(HOME_BP, url_prefix='/')
APP.register_blueprint(BINANCE_BP, url_prefix='/binance/')
