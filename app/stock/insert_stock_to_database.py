import time
from datetime import timezone, datetime

from db_access import db_action


def insert_1day_to_db(list):
    for i in list:
        file_name = i + '.us.txt'
        path = 'G:\Projects\stockpilot-backend\stock_files\\1_day\\' + file_name
        file = open(path, "r")
        ls = []
        a = False
        for x in file:
            if a:
                line = x.split(',')
                year, month, day = line[0].split('-')
                unix_timestamp = int(datetime(int(year), int(month), int(day)).replace(tzinfo=timezone.utc).timestamp()*1000)
                line[0] = unix_timestamp
                line[6] = unix_timestamp
                ls.append(line)
            a = True
        file.close()
        data_obj = {
            "data_1d": ls
        }
        db_action("insert_one", [data_obj, i], "admin")

insert_1day_to_db(['aapl'])
