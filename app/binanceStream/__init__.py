import json
import flask
import requests
from flask import Blueprint
from ..pubsub.data_center import listen_socket,get_history
from getStreamData import update_symbol_set, get_symbol_set
from binance.client import Client


BINANCE_BP = Blueprint('BINANCE_BP', __name__)


@BINANCE_BP.route('/listen/<btc_name>/<interval>', methods=['GET'])
def listen(btc_name,interval):
    def stream(btc_name,interval):
        messages = listen_socket(btc_name,interval)  
        while True:                        
            msg = messages.get()  
            yield msg

    return flask.Response(stream(btc_name,interval), mimetype='text/event-stream')

@BINANCE_BP.route('/historical/<btc_name>/<interval>', methods=['GET'])
def getHistorical(btc_name,interval):
    klines = get_history(btc_name,interval)
    json_klines = json.dumps(klines)
    return json_klines

@BINANCE_BP.route('/add_crypto/<btc_name>', methods=['POST'])
def add_symbols(btc_name):
    return(update_symbol_set(btc_name))


@BINANCE_BP.route('/get_crypto', methods=['GET'])
def get_symbols():
    return(get_symbol_set())

    





# @BINANCE_BP.route('/api/historical/<string:btc_name>', methods=['GET'])
# def getHistorical(btc_name):
#     client = Client()
#     klines = client.get_historical_klines(btc_name, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
#     json_klines = json.dumps(klines)
#     return json_klines

