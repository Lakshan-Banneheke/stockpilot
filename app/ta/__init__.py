from flask import Blueprint

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
