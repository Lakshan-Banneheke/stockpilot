from .ps_model import MessageAnnouncer
from binance.client import Client
from db_access import db_action


announcers = {}

symbols = []

def announce_socket(name,interval,raw_data): # use this function to announce the stream data to the respective user set
    announcers[name][interval].announce(raw_data)

def listen_socket(name,interval): # according to the user input neeeds to listen to the relevent announcer instance
    announcer = announcers[name][interval]
    return(announcer.listen())

def get_history(symbl,interval):
    return(announcers[symbl][interval].get_historical_data(symbl,interval))



def initiate_publisher_set():
    for symbl in symbols:
        announcers[symbl] = {"1d":MessageAnnouncer(),"1h":MessageAnnouncer(),"30m":MessageAnnouncer(),"15m":MessageAnnouncer(),"1m":MessageAnnouncer()}


def initiate_historical_data_set():

    for symbl in symbols:

        client = Client()

        data_1m = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
        data_15m = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_15MINUTE, "1 day ago UTC")
        data_30m = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_30MINUTE, "1 day ago UTC")
        data_1h = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
        data_1d = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1DAY, "1 day ago UTC")

        db_action("remove_many",[{},symbl],"admin")

        db_action("insert_one",[{"type":"data_1m","data":data_1m},symbl],"admin")
        db_action("insert_one",[{"type":"data_15m","data":data_15m},symbl],"admin")
        db_action("insert_one",[{"type":"data_30m","data":data_30m},symbl],"admin")
        db_action("insert_one",[{"type":"data_1h","data":data_1h},symbl],"admin")
        db_action("insert_one",[{"type":"data_1d","data":data_1d},symbl],"admin")

        print("History Set For:",symbl)

    
def initiate_in_memory():

    symbl_set = db_action("read_one",[{"type":"crypto"},"symbols"],"admin")

    for symbl in symbl_set['data']:

        if (symbl not in symbols):

            symbols.append(symbl)
    


def initiate_pub_sub():

    initiate_in_memory()
    initiate_publisher_set()
    initiate_historical_data_set()

    print("PubSub Initiated",symbols)




        
    