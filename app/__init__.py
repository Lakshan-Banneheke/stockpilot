from flask import Flask
from app.crypto import CRYPTO_BP
from app.home import HOME_BP
from app.pubsub.notifications import look_for_nots
from app.stock import STOCK_BP
from app.ta import TA_BP
from app.user import USER_BP
from app.acessWatchList import WLIST_BP
from app.notifications import NOTIFICATIONS_BP
from getStreamData import getStreamData, initiate_get_stream, reboot_binance_connection
from app.pubsub.data_center import initiate_pub_sub
from flask_cors import CORS
from apscheduler.schedulers.background import BackgroundScheduler


def create_app():
    APP = Flask(__name__)
    CORS(APP)

    scheduler = BackgroundScheduler()

    @APP.before_first_request
    def activate_job():
        initiate_get_stream()
        initiate_pub_sub()
        scheduler.add_job(getStreamData)
        scheduler.add_job(look_for_nots,trigger='interval',seconds=10)
        scheduler.add_job(reboot_binance_connection)
        scheduler.start()

    APP.register_blueprint(HOME_BP, url_prefix='/')
    APP.register_blueprint(CRYPTO_BP, url_prefix='/binance/')
    APP.register_blueprint(USER_BP, url_prefix='/user/')
    APP.register_blueprint(TA_BP, url_prefix='/ta/')
    APP.register_blueprint(WLIST_BP, url_prefix='/watchlist/')
    APP.register_blueprint(STOCK_BP, url_prefix='/stock/')
    APP.register_blueprint(NOTIFICATIONS_BP, url_prefix='/notifications/')

    return APP
