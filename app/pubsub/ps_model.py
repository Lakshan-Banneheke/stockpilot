from db_access import db_action
import json
import queue
from . import data_center

class MessageAnnouncer:

    def __init__(self):
        self.listeners = []
        self.db_push_queue =[]

    def listen(self):
        q = queue.Queue(maxsize=1000)
        self.listeners.append(q)
        return q

    def announce(self, msg):

        sy = msg['s']

        state = msg['k']['x']

        typ = "data_" + msg['k']['i']

        open_price = msg['k']['o']

        deocrated_msg_history = [msg['k']['t'],msg['k']['o'],msg['k']['h'],msg['k']['l'],msg['k']['c'],msg['k']['v'],msg['k']['T'],msg['k']['q'],msg['k']['n'],msg['k']['V'],msg['k']['Q'],msg['k']['B']]

        json_msg = json.dumps(msg)

        msg = format_sse(data=json_msg)

        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[i]

        if (typ=="data_1m" and state==True):

            data = db_action("read_one",[{"type":"data_1d"},sy],"admin")
            peak_price = float(data['data'][-1][1])
            percent_price = ((float(open_price) - peak_price)/peak_price)*100

            if (percent_price>75):
                data_center.add_notification({"message":"successful","type":"Over 75 percent incriment","symbol":sy,"open price":open_price,"current peak price":peak_price})
            elif(percent_price>50):
                data_center.add_notification({"message":"successful","type":"Over 50 percent incriment","symbol":sy,"open price":open_price,"current peak price":peak_price})
            elif(percent_price>25):
                data_center.add_notification({"message":"successful","type":"Over 25 percent incriment","symbol":sy,"open price":open_price,"current peak price":peak_price})
            elif(percent_price>1):
                data_center.add_notification({"message":"successful","type":"Over 5 percent incriment","symbol":sy,"open price":open_price,"current peak price":peak_price})
            elif(percent_price<(-25)):
                data_center.add_notification({"message":"successful","type":"Over 25 percent decriment","symbol":sy,"open price":open_price,"current peak price":peak_price})
            elif(percent_price<(-50)):
                data_center.add_notification({"message":"successful","type":"Over 50 percent decriment","symbol":sy,"open price":open_price,"current peak price":peak_price})
            elif(percent_price<(-75)):
                data_center.add_notification({"message":"successful","type":"Over 75 percent decriment","symbol":sy,"open price":open_price,"current peak price":peak_price})

        
        if len(self.db_push_queue)<=10:
            if(state==True):
                self.db_push_queue.append(deocrated_msg_history)
        else:
            hist = db_action("read_one",[{"type":typ},sy],"admin")
            new_data = hist['data']
            for dec_set in self.db_push_queue:
                if (hist['data'][-1][0]<dec_set[0]):
                    new_data.append(dec_set)

            db_action("remove_one",[{"type":typ},sy],"admin")

            db_action("insert_one",[{"type":typ,"data":new_data},sy],"admin")

            print("db updated for",sy,typ,"because Waiting queue filled")

            self.db_push_queue = []
    
    def get_historical_data(self,symbl,interval):

        interval_modified = "data_" + interval

        hist = db_action("read_one",[{"type":interval_modified},symbl],"admin")

        dt_set = hist['data']

        for i in self.db_push_queue:
            if (dt_set[-1][0]<i[0]):
                print(i)
                dt_set.append(i)
                
        return(dt_set)
    
# class NotificationAnnouncer:

#     def __init__(self):
#         self.listener_set = []

#     def listen_nots(self):
#         qu = queue.Queue(maxsize=100)
#         self.listener_set.append(qu)
#         return (qu)

#     def announce_nots(self, msg):

#         msg = format_sse(data=msg)

#         for i in reversed(range(len(self.listener_set))):
#             try:
#                 self.listener_set[i].put_nowait(msg)
#             except queue.Full:
#                 del self.listener_set[i]

def format_sse(data: str, event=None) -> str:
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg