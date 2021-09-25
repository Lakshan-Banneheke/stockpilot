from flask import Blueprint, render_template
import os

STOCK_BP = Blueprint('STOCK_BP', __name__)


@STOCK_BP.route('/', methods=['GET'])
def home():
    return render_template('home/home.html')




