import json
import flask
from flask import Blueprint
from ..pubsub.data_center import listen_socket,get_history,validity_check
from app.utils.getStreamData import get_symbol_set


CRYPTO_BP = Blueprint('CRYPTO_BP', __name__)


@CRYPTO_BP.route('/listen/<btc_name>/<interval>', methods=['GET'])
def listen(btc_name,interval):
    if (validity_check(btc_name,interval)):
        def stream(btc_name,interval):
            messages = listen_socket(btc_name,interval)  
            while True:                        
                msg = messages.get()  
                yield msg

        return flask.Response(stream(btc_name,interval), mimetype='text/event-stream')
    else:
        return({"errmsg":"Invalid Parameters"})

@CRYPTO_BP.route('/historical/<btc_name>/<interval>/<s_date>', methods=['GET'])
def getHistorical(btc_name,interval,s_date):
    if validity_check(btc_name,interval):
        klines = get_history(btc_name,interval,s_date)
        json_klines = json.dumps(klines)
        return json_klines
    else:
        return({"errmsg":"Invalid Parameters"})


@CRYPTO_BP.route('/get_crypto', methods=['GET'])
def get_symbols():
    return(get_symbol_set())



# @CRYPTO_BP.route('/add_crypto/<btc_name>', methods=['POST'])
# def add_symbols(btc_name):
#     return(update_symbol_set(btc_name))

    

