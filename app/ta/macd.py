import json
import talib
from app.ta.utils import get_close_values

def generate_macd(type_name, name, interval):
    close_times, close_prices = get_close_values(type_name, name, interval)
    macd, macdsignal, macdhist = talib.MACD(close_prices)
    dict_macd = dict(zip(close_times[33:], macd[33:]))
    dict_macdsignal = dict(zip(close_times[33:], macdsignal[33:]))
    dict_macdhist = dict(zip(close_times[33:], macdhist[33:]))
    dict_indicator = {'macd': dict_macd, 'macdsignal': dict_macdsignal, 'macdhist': dict_macdhist}
    json_dict = json.dumps(dict_indicator)
    print(json_dict)
    return json_dict
