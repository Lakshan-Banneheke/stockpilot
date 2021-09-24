import json
import talib
from app.ta.utils import get_close_values

def generate_ema():
    #ema for bnb/usdt 1 minute
    close_times, close_prices = get_close_values()
    ema = talib.EMA(close_prices)
    dict_indicator = dict(zip(close_times[29:], ema[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict

def generate_ma():
    #ma for bnb/usdt 1 minute
    close_times, close_prices = get_close_values()
    ma = talib.MA(close_prices)
    dict_indicator = dict(zip(close_times[29:], ma[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict

def generate_sma():
    #sma for bnb/usdt 1 minute
    close_times, close_prices = get_close_values()
    sma = talib.SMA(close_prices)
    dict_indicator = dict(zip(close_times[29:], sma[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict

def generate_wma():
    #wma for bnb/usdt 1 minute
    close_times, close_prices = get_close_values()
    wma = talib.WMA(close_prices)
    dict_indicator = dict(zip(close_times[29:], wma[29:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict