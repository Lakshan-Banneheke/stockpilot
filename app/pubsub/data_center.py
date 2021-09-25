from .ps_model import MessageAnnouncer
from binance.client import Client
import json
from db_access import db_action

announcers = {}

symbols = ["BNBBTC","BNBUSDT"]

def announce_socket(name,interval,raw_data): # use this function to announce the stream data to the respective user set
    announcers[name][interval].announce(raw_data)

def listen_socket(name,interval): # according to the user input neeeds to listen to the relevent announcer instance
    announcer = announcers[name][interval]
    return(announcer.listen())


def initiate_publisher_set():
    for symbl in symbols:
        announcers[symbl] = {"1d":MessageAnnouncer(),"1h":MessageAnnouncer(),"30m":MessageAnnouncer(),"15m":MessageAnnouncer(),"1m":MessageAnnouncer()}


def initiate_historical_data_set():

    for symbl in symbols:

        client = Client()

        data_1m = json.dumps(client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC"))
        data_15m = json.dumps(client.get_historical_klines(symbl, Client.KLINE_INTERVAL_15MINUTE, "1 day ago UTC"))
        data_30m = json.dumps(client.get_historical_klines(symbl, Client.KLINE_INTERVAL_30MINUTE, "1 day ago UTC"))
        data_1h = json.dumps(client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC"))
        data_1d = json.dumps(client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1DAY, "1 day ago UTC"))

        db_action("remove_many",[{},symbl],"admin")

        db_action("insert_one",[{"data_1m":data_1m},symbl],"admin")
        db_action("insert_one",[{"data_15m":data_15m},symbl],"admin")
        db_action("insert_one",[{"data_30m":data_30m},symbl],"admin")
        db_action("insert_one",[{"data_1h":data_1h},symbl],"admin")
        db_action("insert_one",[{"data_1d":data_1d},symbl],"admin")

        print("History Set For:",symbl)
        
    