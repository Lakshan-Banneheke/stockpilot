from flask import Blueprint, render_template
BINANCE_BP = Blueprint('BINANCE_BP', __name__)


@BINANCE_BP.route('/', methods=['GET'])
def binanceStream():
    return render_template('home/home.html')