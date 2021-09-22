from flask import Blueprint, render_template
import os

HOME_BP = Blueprint('HOME_BP', __name__)


@HOME_BP.route('/', methods=['GET'])
def home():
    return render_template('home/home.html')




