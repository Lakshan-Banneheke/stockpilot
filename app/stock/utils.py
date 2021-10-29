from db_access import db_action
from time import time

reverse_date = {"1m":1,"15m":5,"30m":10,"1h":15,"1d":25}


def get_symbol_set():
    symbl_set = db_action("read_one", [{"type": "stock"}, "symbols"], "admin")
    dt = symbl_set['data']
    return {"stock_symbols": dt}


def get_historical_stock_data(symbl, interval, s_date):
    if (s_date == "0000"):
        s_date = round(time() * 1000)

    e_date = int(s_date) - (reverse_date[interval] * 24 * 60 * 60 * 1000)

    coll_name = symbl + "_" + interval

    hist = db_action("read_many", [{"time": {"$gte": int(e_date), "$lt": int(s_date)}}, coll_name], "admin")

    data_pack = []

    time_stamps = []

    for val in hist:
        if (val['data'][0] not in time_stamps):
            time_stamps.append(val['data'][0])
            data_pack.append(val['data'])

    return data_pack

