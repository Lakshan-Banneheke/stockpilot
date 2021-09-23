from flask import Flask
from app.home import HOME_BP
from app.binanceStream import BINANCE_BP
from app.ta import TA_BP
from app.user import USER_BP
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
APP.register_blueprint(USER_BP, url_prefix='/user/')
APP.register_blueprint(TA_BP, url_prefix='/ta/')