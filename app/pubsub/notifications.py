from time import time
import json
from db_access import db_action
from firebase_config import sendPush

notifications = []
app_tokens = []

def listen_notifications(device_token, email):
    watchList = db_action("read_one", [{"email_id": email}, "watch_list"], "admin")
    print(watchList['brands'])
    # state = db_action("insert_one", [{"token": token}, "tokens"], "admin")
    if watchList:
        return "Successfully Registered for Notifications"
    else:
        return "Error in registering please retry"


def add_notification(data):
    notifications.append(data)


def look_for_nots():
    if len(notifications) > 0:
        sendPush("New Notification", json.dumps(notifications[0]), app_tokens)
        db_action("insert_one", [{"time": int(time() * 1000), "data": notifications[0]}, "notifications"], "admin")
        print("Notifications Send")
        notifications.pop(0)


def historical_nots():
    time_filter = int(time() * 1000 - (5 * 24 * 60 * 60 * 1000))
    data = db_action("read_many", [{"time": {"$gte": time_filter}}, "notifications"], "admin")
    opt = []
    for dt in data:
        opt.append([dt['time'], dt['data']])

    for dt in notifications:
        opt.append([int(time() * 1000), dt])

    return {"last 5 days notifications": opt}

