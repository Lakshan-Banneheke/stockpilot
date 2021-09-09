from flask import Flask
from app.home import HOME_BP
from app.binanceStream import BINANCE_BP
from getStreamData import getStreamData


APP = Flask(__name__)


@APP.before_first_request
def activate_job():
    getStreamData()


APP.register_blueprint(HOME_BP, url_prefix='/')
APP.register_blueprint(BINANCE_BP, url_prefix='/binance/')