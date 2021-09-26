from db_access import db_action
import json
import queue

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

        deocrated_msg_history = [msg['k']['t'],msg['k']['o'],msg['k']['h'],msg['k']['l'],msg['k']['c'],msg['k']['v'],msg['k']['T'],msg['k']['q'],msg['k']['n'],msg['k']['V'],msg['k']['Q'],msg['k']['B']]

        json_msg = json.dumps(msg)

        msg = format_sse(data=json_msg)

        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[i]
        
        if len(self.db_push_queue)<=10:
            if(state==True):
                self.db_push_queue.append(deocrated_msg_history)
        else:
            hist = db_action("read_one",[{"type":typ},sy],"admin")
            new_data = hist['data']
            for dec_set in self.db_push_queue:
                if (hist['data'][-1][0]<dec_set[0]):
                    new_data.append(dec_set)
            db_action("update_one",[{"type":typ},{"$set":{"data":new_data}},sy],"admin")
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




def format_sse(data: str, event=None) -> str:
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg