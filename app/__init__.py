from flask import Flask
from app.home import HOME_BP
from app.binanceStream import BINANCE_BP
from getStreamData import getStreamData
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler


APP = Flask(__name__)
CORS(APP)

scheduler = BackgroundScheduler()


@APP.before_first_request
def activate_job():
    scheduler.add_job(getStreamData)
    scheduler.start()


APP.register_blueprint(HOME_BP, url_prefix='/')
APP.register_blueprint(BINANCE_BP, url_prefix='/binance/')