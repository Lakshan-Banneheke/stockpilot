from binance import ThreadedWebsocketManager
from flask import Blueprint, render_template
BINANCE_BP = Blueprint('BINANCE_BP', __name__)


@BINANCE_BP.route('/', methods=['GET'])
def binanceStream():
    symbol = 'BTCUSDT'

    twm = ThreadedWebsocketManager()
    # start is required to initialise its internal loop
    twm.start()

    def handle_socket_message(msg):
        print(f"message type: {msg['e']}")
        print(msg)

    twm.start_kline_socket(callback=handle_socket_message, symbol=symbol)

    return render_template('home/home.html')