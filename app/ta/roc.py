import json
import talib
from app.ta.utils import get_close_values

def generate_roc(type_name, name, interval):
    close_times, close_prices = get_close_values(type_name, name, interval)
    roc = talib.ROC(close_prices)
    dict_indicator = dict(zip(close_times[10:], roc[10:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict

