from binance.client import Client
import numpy as np


def get_close_values():
    client = Client()
    klines = client.get_historical_klines('BNBUSDT', Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
    close_prices = np.array([i[4] for i in klines], dtype=float)
    close_times = [i[6] for i in klines]
    return close_times, close_prices
