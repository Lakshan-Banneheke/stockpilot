from aiohttp.client import request
from binance import exceptions
from db_access import db_action
import json
import queue
from . import notifications
from . import db_feed
from binance.client import Client


class MessageAnnouncer:

    def __init__(self):
        self.listeners = []
        try:
            self.client = Client()
        except Exception as e:
            print("check network")

    def listen(self):
        q = queue.Queue(maxsize=20)
        self.listeners.append(q)
        return q

    def announce(self, msg):

        sy = msg['s']

        coll_name = sy + "_" + msg['k']['i']

        state = msg['k']['x']

        typ = "data_" + msg['k']['i']

        open_price = msg['k']['o']

        deocrated_msg_history = [msg['k']['t'], msg['k']['o'], msg['k']['h'], msg['k']['l'], msg['k']['c'],
                                 msg['k']['v'], msg['k']['T'], msg['k']['q'], msg['k']['n'], msg['k']['V'],
                                 msg['k']['Q'], msg['k']['B']]

        json_msg = json.dumps(msg)

        msg = format_sse(data=json_msg)

        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[i]

        try:

            if (typ == "data_1m" and state == True):

                data = self.client.get_historical_klines(sy, Client.KLINE_INTERVAL_1DAY, "1 day ago UTC")

                peak_price = float(data[0][1])

                percent_price = ((float(open_price) - peak_price) / peak_price) * 100

                if (percent_price > 75):
                    notifications.add_notification(
                        {"message": "successful", "type": "Over 75 percent incriment", "symbol": sy,
                        "open price": open_price, "current peak price": peak_price})
                elif (percent_price > 50):
                    notifications.add_notification(
                        {"message": "successful", "type": "Over 50 percent incriment", "symbol": sy,
                        "open price": open_price, "current peak price": peak_price})
                elif (percent_price > 25):
                    notifications.add_notification(
                        {"message": "successful", "type": "Over 25 percent incriment", "symbol": sy,
                        "open price": open_price, "current peak price": peak_price})
                elif (percent_price > 5):
                    notifications.add_notification({"message": "successful", "type": "Over 5 percent incriment", "symbol": sy,
                                                "open price": open_price, "current peak price": peak_price})
                elif (percent_price < (-25)):
                    notifications.add_notification(
                        {"message": "successful", "type": "Over 25 percent decriment", "symbol": sy,
                        "open price": open_price, "current peak price": peak_price})
                elif (percent_price < (-50)):
                    notifications.add_notification(
                        {"message": "successful", "type": "Over 50 percent decriment", "symbol": sy,
                        "open price": open_price, "current peak price": peak_price})
                elif (percent_price < (-75)):
                    notifications.add_notification(
                        {"message": "successful", "type": "Over 75 percent decriment", "symbol": sy,
                        "open price": open_price, "current peak price": peak_price})
        
        except Exception as e:

            print("Notification send Failed Check the network connection")
                    

        if (state == True):
            time_stamp = deocrated_msg_history[0]
            db_feed.add_to_db_feed([time_stamp,coll_name,deocrated_msg_history])
            

    def get_historical_data(self, symbl, interval, start_date, end_data):

        coll_name = symbl + "_" + interval

        hist = db_action("read_many", [{"time": {"$gte": end_data, "$lt": start_date}}, coll_name], "admin")

        if hist != "Error":

            data_pack = []

            time_stamps =[]

            for val in hist:
                if (val['data'][0] not in time_stamps):
                    time_stamps.append(val['data'][0])
                    data_pack.append(val['data'])
                    
            return(data_pack)

        else:
            print("Error in History Getter")
            return("Error")

class NotificationAnnouncer:

    def __init__(self):
        self.listener_set = []

    def listen_nots(self):
        qu = queue.Queue(maxsize=100)
        self.listener_set.append(qu)
        return (qu)

    def announce_nots(self, msg):

        msg = format_sse(data=msg)

        for i in reversed(range(len(self.listener_set))):
            try:
                self.listener_set[i].put_nowait(msg)
            except queue.Full:
                del self.listener_set[i]


def format_sse(data: str, event=None) -> str:
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg