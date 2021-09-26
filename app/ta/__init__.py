from flask import Blueprint

from app.ta.bbands import generate_bbands
from app.ta.macd import generate_macd
from app.ta.moving_averages import generate_wma, generate_sma, generate_ma, generate_ema
from app.ta.obv import generate_obv
from app.ta.roc import generate_roc
from app.ta.rsi import generate_rsi
from app.ta.stoch import generate_stoch

TA_BP = Blueprint('TA_BP', __name__)


@TA_BP.route('/rsi/<type_name>/<name>/<interval>', methods=['GET'])
def get_rsi(type_name, name, interval):
    return generate_rsi(type_name, name, interval)


@TA_BP.route('/obv/<type_name>/<name>/<interval>', methods=['GET'])
def get_obv(type_name, name, interval):
    return generate_obv(type_name, name, interval)


@TA_BP.route('/roc/<type_name>/<name>/<interval>', methods=['GET'])
def get_roc(type_name, name, interval):
    return generate_roc(type_name, name, interval)


@TA_BP.route('/ema/<type_name>/<name>/<interval>', methods=['GET'])
def get_ema(type_name, name, interval):
    return generate_ema(type_name, name, interval)


@TA_BP.route('/ma/<type_name>/<name>/<interval>', methods=['GET'])
def get_ma(type_name, name, interval):
    return generate_ma(type_name, name, interval)


@TA_BP.route('/sma/<type_name>/<name>/<interval>', methods=['GET'])
def get_sma(type_name, name, interval):
    return generate_sma(type_name, name, interval)


@TA_BP.route('/wma/<type_name>/<name>/<interval>', methods=['GET'])
def get_wma(type_name, name, interval):
    return generate_wma(type_name, name, interval)


@TA_BP.route('/stoch/<type_name>/<name>/<interval>', methods=['GET'])
def get_stoch(type_name, name, interval):
    return generate_stoch(type_name, name, interval)


@TA_BP.route('/bbands/<type_name>/<name>/<interval>', methods=['GET'])
def get_bbands(type_name, name, interval):
    return generate_bbands(type_name, name, interval)


@TA_BP.route('/macd/<type_name>/<name>/<interval>', methods=['GET'])
def get_macd(type_name, name, interval):
    return generate_macd(type_name, name, interval)
