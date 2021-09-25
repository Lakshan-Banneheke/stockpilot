import json
import flask
import requests
from flask import Blueprint, render_template
from ..pubsub.data_center import listen_socket
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

@BINANCE_BP.route('/api/historical/<string:btc_name>', methods=['GET'])
def getHistorical(btc_name):
    client = Client()
    klines = client.get_historical_klines(btc_name, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    json_klines = json.dumps(klines)
    return json_klines
