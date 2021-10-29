import json
import talib
from app.ta.utils import get_close_values


def generate_ema(type_name, name, interval, s_date):
    close_times, close_prices = get_close_values(type_name, name, interval, s_date)
    ema = talib.EMA(close_prices)
    dict_indicator = dict(zip(close_times[29:], ema[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict


def generate_ma(type_name, name, interval, s_date):
    close_times, close_prices = get_close_values(type_name, name, interval, s_date)
    ma = talib.MA(close_prices)
    dict_indicator = dict(zip(close_times[29:], ma[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict


def generate_sma(type_name, name, interval, s_date):
    close_times, close_prices = get_close_values(type_name, name, interval, s_date)
    sma = talib.SMA(close_prices)
    dict_indicator = dict(zip(close_times[29:], sma[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict


def generate_wma(type_name, name, interval, s_date):
    close_times, close_prices = get_close_values(type_name, name, interval, s_date)
    wma = talib.WMA(close_prices)
    dict_indicator = dict(zip(close_times[29:], wma[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict
