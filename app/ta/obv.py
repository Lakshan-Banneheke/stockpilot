import json
import talib

from app.ta.utils import get_close_and_volume_values


def generate_obv(type_name, name, interval):
    close_times, volume, close_prices = get_close_and_volume_values(type_name, name, interval)
    obv = talib.OBV(close_prices, volume)
    dict_indicator = dict(zip(close_times, obv))
    json_dict = json.dumps(dict_indicator)
    return json_dict

