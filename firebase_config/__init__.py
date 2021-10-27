import firebase_admin
from firebase_admin import credentials, messaging
import os

from db_access import db_action

current_direc = os.getcwd()
path_name = os.path.join(current_direc,"serviceKey.json")

cred = credentials.Certificate(path_name)
firebase_admin.initialize_app(cred)

def sendPush(notification, symbol):

    title = symbol + ' - ' + notification['type']
    body = 'Peak Price: ' + str(notification['current peak price']) + '\n' + 'Open Price: ' + str(notification['open price'])
    data = {"data": title + '\n' + body}

    result = db_action("read_one", [{"type": symbol}, "notif_tokens"], "admin")
    if result:
        tokens = result['tokens']
        print(title)
        print(body)
        # See documentation on defining a message payload.
        message = messaging.MulticastMessage(
            notification=messaging.Notification(
                title=title,
                body=body
            ),
            data=data,
            tokens=tokens,
        )

        # Send a message to the device corresponding to the provided
        # registration token.
        response = messaging.send_multicast(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)