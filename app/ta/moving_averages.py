import json

import numpy as np
import talib
from app.ta.utils import get_close_values


def generate_ema(type_name, name, interval, s_date):
    close_times, close_prices = get_close_values(type_name, name, interval, s_date)

    if len(close_times) == 0:
        return {'error': 'No values'}

    ema = talib.EMA(close_prices)

    a = 0
    for i in range(ema.size):
        if not np.isnan(ema[i]):
            a = i
            break
    dict_indicator = dict(zip(close_times[a:], ema[a:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict


def generate_ma(type_name, name, interval, s_date):
    close_times, close_prices = get_close_values(type_name, name, interval, s_date)

    if len(close_times) == 0:
        return {'error': 'No values'}

    ma = talib.MA(close_prices)
    a = 0
    for i in range(ma.size):
        if not np.isnan(ma[i]):
            a = i
            break
    dict_indicator = dict(zip(close_times[a:], ma[a:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict


def generate_sma(type_name, name, interval, s_date):
    close_times, close_prices = get_close_values(type_name, name, interval, s_date)
    if len(close_times) == 0:
        return {'error': 'No values'}

    sma = talib.SMA(close_prices)
    a = 0
    for i in range(sma.size):
        if not np.isnan(sma[i]):
            a = i
            break
    dict_indicator = dict(zip(close_times[a:], sma[a:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict


def generate_wma(type_name, name, interval, s_date):
    close_times, close_prices = get_close_values(type_name, name, interval, s_date)
    if len(close_times) == 0:
        return {'error': 'No values'}

    wma = talib.WMA(close_prices)
    a = 0
    for i in range(wma.size):
        if not np.isnan(wma[i]):
            a = i
            break
    dict_indicator = dict(zip(close_times[a:], wma[a:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict
