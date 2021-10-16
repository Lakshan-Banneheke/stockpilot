import json
import flask
import requests
from flask import Blueprint
from ..pubsub.data_center import listen_socket,get_history
from getStreamData import get_symbol_set
from binance.client import Client


CRYPTO_BP = Blueprint('CRYPTO_BP', __name__)


@CRYPTO_BP.route('/listen/<btc_name>/<interval>', methods=['GET'])
def listen(btc_name,interval):
    def stream(btc_name,interval):
        messages = listen_socket(btc_name,interval)  
        while True:                        
            msg = messages.get()  
            yield msg

    return flask.Response(stream(btc_name,interval), mimetype='text/event-stream')

@CRYPTO_BP.route('/historical/<btc_name>/<interval>/<s_date>/<e_date>', methods=['GET'])
def getHistorical(btc_name,interval,s_date,e_date):
    klines = get_history(btc_name,interval,s_date,e_date)
    json_klines = json.dumps(klines)
    return json_klines


@CRYPTO_BP.route('/get_crypto', methods=['GET'])
def get_symbols():
    return(get_symbol_set())



# @CRYPTO_BP.route('/add_crypto/<btc_name>', methods=['POST'])
# def add_symbols(btc_name):
#     return(update_symbol_set(btc_name))

    

