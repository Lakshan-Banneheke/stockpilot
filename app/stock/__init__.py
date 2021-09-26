import json

from flask import Blueprint, render_template
import os

from app.stock.utils import get_symbol_set, get_historical_stock_data

STOCK_BP = Blueprint('STOCK_BP', __name__)


@STOCK_BP.route('/historical/<stock_name>/<interval>', methods=['GET'])
def getHistorical(stock_name, interval):
    klines = get_historical_stock_data(stock_name, interval)
    json_klines = json.dumps(klines)
    return json_klines


@STOCK_BP.route('/get_stock_list', methods=['GET'])
def get_symbols():
    return get_symbol_set()
