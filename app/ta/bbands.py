import json

import numpy as np
import talib
from app.ta.utils import get_close_values

def generate_bbands(type_name, name, interval, s_date):
    close_times, close_prices = get_close_values(type_name, name, interval, s_date)
    if len(close_times) == 0:
        return {'error': 'No values'}

    upperband, middleband, lowerband = talib.BBANDS(close_prices)
    a = 0
    for i in range(upperband.size):
        if not np.isnan(upperband[i]):
            a = i
            break

    dict_upperband = dict(zip(close_times[a:], upperband[a:]))
    dict_middleband = dict(zip(close_times[a:], middleband[a:]))
    dict_lowerband = dict(zip(close_times[a:], lowerband[a:]))
    dict_indicator = {'upperband': dict_upperband, 'middleband': dict_middleband, 'lowerband': dict_lowerband}
    json_dict = json.dumps(dict_indicator)
    return json_dict

