import json
import talib

from app.ta.utils import get_high_low_close_values


def generate_stoch(type_name, name, interval):
    high_prices, low_prices, close_prices, close_times = get_high_low_close_values(type_name, name, interval)
    slowk, slowd = talib.STOCH(high_prices, low_prices, close_prices)
    slowk_dict = dict(zip(close_times[8:], slowk[8:]))
    slowd_dict = dict(zip(close_times[8:], slowd[8:]))
    dict_indicator = {'slowk': slowk_dict, 'slowd': slowd_dict}
    json_dict = json.dumps(dict_indicator)
    return json_dict

