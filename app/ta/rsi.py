import json
import talib
from app.ta.utils import get_close_values

def generate_rsi():
    #rsi for bnb/usdt 1 minute
    close_times, close_prices = get_close_values()
    rsi = talib.RSI(close_prices)
    time_rsi = dict(zip(close_times[14:], rsi[14:]))
    json_time_rsi = json.dumps(time_rsi)
    return json_time_rsi


