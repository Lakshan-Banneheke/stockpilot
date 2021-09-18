import json

import flask
import requests
from flask import Blueprint, render_template
from ..pubsub.data_center import listen_socket
from binance.client import Client


BINANCE_BP = Blueprint('BINANCE_BP', __name__)


@BINANCE_BP.route('/', methods=['GET'])
def binanceStream():
    return render_template('home/home.html')


@BINANCE_BP.route('/listen/<string:btc_name>', methods=['GET'])
def listen(btc_name):
    def stream(btc_name):
        messages = listen_socket(btc_name)  
        while True:                        
            msg = messages.get()  
            yield msg

    return flask.Response(stream(btc_name), mimetype='text/event-stream')

@BINANCE_BP.route('/api/historical/<string:btc_name>', methods=['GET'])
def getHistorical(btc_name):
    client = Client()
    klines = client.get_historical_klines(btc_name, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    json_klines = json.dumps(klines)
    return json_klines
