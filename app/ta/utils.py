import numpy as np

from app.pubsub.data_center import get_history
from app.stock import get_historical_stock_data


def get_close_values(type_name, name, interval, s_date):
    if type_name == 'crypto':
        klines = get_history(name, interval, s_date)
    else:
        klines = get_historical_stock_data(name, interval, s_date)
    close_prices = np.array([i[4] for i in klines], dtype=float)
    close_times = [i[6] + 1 for i in klines]
    return close_times, close_prices


def get_close_and_volume_values(type_name, name, interval, s_date):
    if type_name == 'crypto':
        klines = get_history(name, interval, s_date)
    else:
        klines = get_historical_stock_data(name, interval, s_date)
    close_prices = np.array([i[4] for i in klines], dtype=float)
    volume = np.array([i[5] for i in klines], dtype=float)
    close_times = [i[6] + 1 for i in klines]
    return close_times, volume, close_prices

def get_high_low_close_values(type_name, name, interval, s_date):
    if type_name == 'crypto':
        klines = get_history(name, interval, s_date)
    else:
        klines = get_historical_stock_data(name, interval, s_date)
    high_prices = np.array([i[2] for i in klines], dtype=float)
    low_prices = np.array([i[3] for i in klines], dtype=float)
    close_prices = np.array([i[4] for i in klines], dtype=float)
    close_times = [i[6] + 1 for i in klines]
    return high_prices, low_prices, close_prices, close_times
