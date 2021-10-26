from flask import Blueprint, request
import json
from app.pubsub.notifications import listen_notifications, historical_nots
from app.user import token_required

NOTIFICATIONS_BP = Blueprint('NOTIFICATIONS_BP', __name__)

@NOTIFICATIONS_BP.route('/listen_nots/open_price', methods=['POST'])
@token_required
def register_to_notifications(current_user):
    data = json.loads(request.data, strict=False)
    device_token = data['device_token']

    return listen_notifications(device_token, current_user['email'])

@NOTIFICATIONS_BP.route('/historical_nots/open_price', methods=['GET'])
def get_history_nots():
    return historical_nots()
