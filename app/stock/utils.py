from db_access import db_action
from time import time

Change reverse_date = {"5m":5,"30m":10,"1h":15,"1d":25}


def get_symbol_set():
    symbl_set = db_action("read_one", [{"type": "stock"}, "symbols"], "admin")
    dt = symbl_set['data']
    return {"stock_symbols": dt}


def get_historical_stock_data(symbl, interval, s_date):
    coll_name = symbl + "_" + interval
    last_item = db_action("find_last_entry", [coll_name], "admin")

    if (s_date == "0000"):
        s_date = int(last_item[0]['time'])

    e_date = int(s_date) - (reverse_date[interval] * 24 * 60 * 60 * 1000)

    print(s_date)
    print(e_date)



    hist = db_action("read_many", [{"time": {"$gte": int(e_date), "$lt": int(s_date)}}, coll_name], "admin")

    data_pack = []

    time_stamps = []

    for val in hist:
        if (val['data'][0] not in time_stamps):
            time_stamps.append(val['data'][0])
            data_pack.append(val['data'])

    return data_pack

