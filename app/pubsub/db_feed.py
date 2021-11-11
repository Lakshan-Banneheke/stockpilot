
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
                db_action("insert_one", [{"time": data[0], "data": data[2]}, data[1]],"admin")
                print("db updated for", data[1], "due interval closing")
            except Exception:
                print("DB Feed Error")
        else:
            time.sleep(20)


# check = db_action("read_one", [{"time": deocrated_msg_history[0]}, coll_name], "admin")
            # if check != "Error":
            #     if (check):
            #         req_doc = {"time": deocrated_msg_history[0]}
            #         new_data = {"$set": {"data": deocrated_msg_history}}

            #         db_action("update_one", [req_doc, new_data, coll_name], "admin")
            #         print("db updated for", sy, typ, "due interval closing")
            #     else:
            #         db_action("insert_one", [{"time": deocrated_msg_history[0], "data": deocrated_msg_history}, coll_name],"admin")
            #         print("db updated for", sy, typ, "due interval closing")