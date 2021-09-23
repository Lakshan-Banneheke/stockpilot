from flask import Blueprint

from app.ta.rsi import generate_rsi

TA_BP = Blueprint('TA_BP', __name__)


@TA_BP.route('/rsi', methods=['GET'])
def get_rsi():
    return generate_rsi()




