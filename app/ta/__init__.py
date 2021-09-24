from flask import Blueprint

from app.ta.moving_averages import generate_wma, generate_sma, generate_ma, generate_ema
from app.ta.obv import generate_obv
from app.ta.roc import generate_roc
from app.ta.rsi import generate_rsi

TA_BP = Blueprint('TA_BP', __name__)


@TA_BP.route('/rsi', methods=['GET'])
def get_rsi():
    return generate_rsi()


@TA_BP.route('/obv', methods=['GET'])
def get_obv():
    return generate_obv()


@TA_BP.route('/roc', methods=['GET'])
def get_roc():
    return generate_roc()


@TA_BP.route('/ema', methods=['GET'])
def get_ema():
    return generate_ema()


@TA_BP.route('/ma', methods=['GET'])
def get_ma():
    return generate_ma()


@TA_BP.route('/sma', methods=['GET'])
def get_sma():
    return generate_sma()


@TA_BP.route('/wma', methods=['GET'])
def get_wma():
    return generate_wma()
