import json
import talib

from app.ta.utils import get_close_and_volume_values


def generate_obv():
    #obv for bnb/usdt 1 minute
    close_times, volume, close_prices = get_close_and_volume_values()
    obv = talib.OBV(close_prices, volume)
    print(obv)
    dict_indicator = dict(zip(close_times, obv))
    json_dict = json.dumps(dict_indicator)
    return json_dict

