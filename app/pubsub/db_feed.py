
import time
from db_access import db_action


dbFeed = []


def add_to_db_feed(data):
    dbFeed.append(data)

def do_db_feed():
    while True:
        if len(dbFeed)>0:
            try:
                data = dbFeed.pop(0)
                result = db_action("insert_one", [{"time": data[0], "data": data[2]}, data[1]],"admin")
                if(result!="Error"):
                    print("db updated for", data[1], "due interval closing")
            except Exception:
                print("DB Feed Error")
        else:
            time.sleep(20)


