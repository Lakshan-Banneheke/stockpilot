import flask
from flask import Blueprint, request
from ..pubsub.data_center import historical_nots,listen_notifications
import json

NOTIFICATIONS_BP = Blueprint('NOTIFICATIONS_BP', __name__)



@NOTIFICATIONS_BP.route('/listen_nots/open_price', methods=['POST'])
def register_to_notifications():
    data = json.loads(request.data, strict=False)
    return(listen_notifications(data['token']))

@NOTIFICATIONS_BP.route('/historical_nots/open_price', methods=['GET'])
def get_history_nots():
    return(historical_nots())
