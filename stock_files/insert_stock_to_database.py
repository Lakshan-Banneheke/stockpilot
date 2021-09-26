import json
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
            "type": "data_1d",
            "data": ls
        }
        db_action("insert_one", [data_obj, i], "admin")

def insert_1hour_to_db(list):
    for i in list:
        file_name = i + '.us.txt'
        path = 'G:\Projects\stockpilot-backend\stock_files\\1_hour\\' + file_name
        file = open(path, "r")
        ls = []
        a = False
        for x in file:
            if a:
                line = x.split(',')
                datetime_val = line[0] + ' ' + line[1]
                unix_timestamp = int(datetime.strptime(datetime_val, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc).timestamp()*1000)
                line = line[1:]
                line[0] = unix_timestamp
                line[6] = unix_timestamp
                ls.append(line)
            a = True
        file.close()
        data_obj = {
            "type": 'data_1h',
            "data": ls
        }

        db_action("insert_one", [data_obj, i], "admin")

def insert_5min_to_db(list):
    for i in list:
        file_name = i + '.us.txt'
        path = 'G:\Projects\stockpilot-backend\stock_files\\5_min\\' + file_name
        file = open(path, "r")
        ls = []
        a = False
        for x in file:
            if a:
                line = x.split(',')
                datetime_val = line[0] + ' ' + line[1]
                unix_timestamp = int(datetime.strptime(datetime_val, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc).timestamp()*1000)
                line = line[1:]
                line[0] = unix_timestamp
                line[6] = unix_timestamp
                ls.append(line)
            a = True
        file.close()
        data_obj = {
            "type": 'data_5m',
            "data": ls
        }
        db_action("insert_one", [data_obj, i], "admin")

def delete(ls):
    for i in ls:
        db_action("delete_collection", [i], "admin")

def add_stock(ls):
    data_obj = {
        "type": "stock",
        "data": ls
    }
    db_action("insert_one", [data_obj, 'symbols'], "admin")


# insert_1day_to_db(['aapl', 'msft', 'goog', 'amzn', 'fb', 'tsla', 'brk-a', 'nvda', 'v', 'jpm', 'jnj', 'baba', 'wmt', 'unh', 'hd'])
# insert_1hour_to_db(['aapl', 'msft', 'goog', 'amzn', 'fb', 'tsla', 'brk-a', 'nvda', 'v', 'jpm', 'jnj', 'baba', 'wmt', 'unh', 'hd'])
# insert_5min_to_db(['aapl', 'msft', 'goog', 'amzn', 'fb', 'tsla', 'brk-a', 'nvda', 'v', 'jpm', 'jnj', 'baba', 'wmt', 'unh', 'hd'])

# delete(['aapl', 'msft', 'goog', 'amzn', 'fb', 'tsla', 'brk-a', 'nvda', 'v', 'jpm', 'jnj', 'baba', 'wmt', 'unh', 'hd'])

# add_stock(['aapl', 'msft', 'goog', 'amzn', 'fb', 'tsla', 'brk-a', 'nvda', 'v', 'jpm', 'jnj', 'baba', 'wmt', 'unh', 'hd'])
