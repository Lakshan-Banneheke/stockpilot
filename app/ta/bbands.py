import json
import talib
from app.ta.utils import get_close_values

def generate_bbands(type_name, name, interval):
    close_times, close_prices = get_close_values(type_name, name, interval)
    upperband, middleband, lowerband = talib.BBANDS(close_prices)
    dict_upperband = dict(zip(close_times[10:], upperband[10:]))
    dict_middleband = dict(zip(close_times[10:], middleband[10:]))
    dict_lowerband = dict(zip(close_times[10:], lowerband[10:]))
    dict_indicator = {'upperband': dict_upperband, 'middleband': dict_middleband, 'lowerband': dict_lowerband}
    json_dict = json.dumps(dict_indicator)
    return json_dict


