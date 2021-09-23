import json
import talib
from app.ta.utils import get_close_values

def generate_roc():
    #roc for bnb/usdt 1 minute
    close_times, close_prices = get_close_values()
    roc = talib.ROC(close_prices)
    dict_indicator = dict(zip(close_times[10:], roc[10:]))
    json_dict = json.dumps(dict_indicator)
    return json_dict

