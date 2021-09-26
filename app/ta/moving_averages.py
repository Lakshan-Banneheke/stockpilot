import json
import talib
from app.ta.utils import get_close_values


def generate_ema(type_name, name, interval):
    close_times, close_prices = get_close_values(type_name, name, interval)
    ema = talib.EMA(close_prices)
    dict_indicator = dict(zip(close_times[29:], ema[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict


def generate_ma(type_name, name, interval):
    close_times, close_prices = get_close_values(type_name, name, interval)
    ma = talib.MA(close_prices)
    dict_indicator = dict(zip(close_times[29:], ma[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict


def generate_sma(type_name, name, interval):
    close_times, close_prices = get_close_values(type_name, name, interval)
    sma = talib.SMA(close_prices)
    dict_indicator = dict(zip(close_times[29:], sma[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict


def generate_wma(type_name, name, interval):
    close_times, close_prices = get_close_values(type_name, name, interval)
    wma = talib.WMA(close_prices)
    dict_indicator = dict(zip(close_times[29:], wma[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict
