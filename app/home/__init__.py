from flask import Blueprint, render_template
import flask
from ..pubsub.data_center import listen_socket,announce_socket

HOME_BP = Blueprint('HOME_BP', __name__)


@HOME_BP.route('/', methods=['GET'])
def home():
    return render_template('home/home.html')

@HOME_BP.route('/listen', methods=['GET'])
def listen():
    def stream():
        messages = listen_socket("check")  #Check is a dummy to represent the crypto stream that the user wants to listen. Need to get that value from the url and replace
        while True:                        #Check the data_center.py need to complete that file
            msg = messages.get()  
            yield msg

    return flask.Response(stream(), mimetype='text/event-stream')



@HOME_BP.route('/ping', methods=['GET']) # Not used, here to check the announcing capability dont use as an endpoint
def ping():
    announce_socket()
    return({},200)