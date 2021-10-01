import flask
from flask import Blueprint
from ..pubsub.data_center import listen_notifications, historical_nots

NOTIFICATIONS_BP = Blueprint('NOTIFICATIONS_BP', __name__)


@NOTIFICATIONS_BP.route('/listen_nots/open_price', methods=['GET'])
def listenn():
    def stream():
        notifications = listen_notifications()
        while True:                        
            msg = notifications.get()  
            yield msg

    return flask.Response(stream(), mimetype='text/event-stream')


@NOTIFICATIONS_BP.route('/historical_nots/open_price', methods=['GET'])
def get_history_nots():
    return(historical_nots())
