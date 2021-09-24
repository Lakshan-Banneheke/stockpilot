from binance.client import Client
import numpy as np


def get_close_values():
    client = Client()
    klines = client.get_historical_klines('BNBUSDT', Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    close_prices = np.array([i[4] for i in klines], dtype=float)
    close_times = [i[6] for i in klines]
    return close_times, close_prices


def get_close_and_volume_values():
    client = Client()
    klines = client.get_historical_klines('BNBUSDT', Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    close_prices = np.array([i[4] for i in klines], dtype=float)
    volume = np.array([i[5] for i in klines], dtype=float)
    close_times = [i[6] for i in klines]
    return close_times, volume, close_prices

def get_high_low_close_values():
    client = Client()
    klines = client.get_historical_klines('BNBUSDT', Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    high_prices = np.array([i[2] for i in klines], dtype=float)
    low_prices = np.array([i[3] for i in klines], dtype=float)
    close_prices = np.array([i[4] for i in klines], dtype=float)
    close_times = [i[6] for i in klines]
    return high_prices, low_prices, close_prices, close_times
