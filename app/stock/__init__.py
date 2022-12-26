import json
from flask import Blueprint


from app.stock.utils import get_symbol_set, get_historical_stock_data

STOCK_BP = Blueprint('STOCK_BP', __name__)


@STOCK_BP.route('/historical/<stock_name>/<interval>/<s_date>', methods=['GET'])
def getHistoricalStock(stock_name, interval, s_date):
    klines = get_historical_stock_data(stock_name, interval, s_date)
    json_klines = json.dumps(klines)
    return json_klines


@STOCK_BP.route('/get_stock_list', methods=['GET'])
def get_symbols():
    return get_symbol_set()
