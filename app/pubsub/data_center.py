from .ps_model import MessageAnnouncer
from binance.client import Client
from db_access import db_action
from time import time
announcers = {}

client = Client()

symbols = []

reverse_date = {"1m":1,"15m":5,"30m":10,"1h":15,"1d":25}

period_set = ["1m","15m","30m","1h","1d"]

############################################################################ Functions related to the live listening of Crypto data Starts

def announce_socket(name,interval,raw_data): # use this function to announce the stream data to the respective user set
    announcers[name][interval].announce(raw_data)


def listen_socket(name,interval): # according to the user input neeeds to listen to the relevent announcer instance
    announcer = announcers[name][interval]
    return(announcer.listen())


def get_history(symbl,interval,s_date):

    if (s_date == "0000"):
        s_date = round(time() * 1000)
    e_date = int(s_date) - (reverse_date[interval]*24*60*60*1000)
    return(announcers[symbl][interval].get_historical_data(symbl,interval,int(s_date),int(e_date)))
    

############################################################################ Functions related to the live listening of Crypto data Ends

############################################################################ Initiation Logic Starts

def initiate_publisher_set():
    for symbl in symbols:
        announcers[symbl] = {"1d":MessageAnnouncer(),"1h":MessageAnnouncer(),"30m":MessageAnnouncer(),"15m":MessageAnnouncer(),"1m":MessageAnnouncer()}

def initiate_historical_data_set():

    for symbl in symbols:

        time_1m = get_last_time(symbl,"1m")
        time_15m = get_last_time(symbl,"15m")
        time_30m = get_last_time(symbl,"30m")
        time_1h = get_last_time(symbl,"1h")
        time_1d = get_last_time(symbl,"1d")

        data_1m = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1MINUTE, time_1m)
        data_15m = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_15MINUTE, time_15m)
        data_30m = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_30MINUTE, time_30m)
        data_1h = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1HOUR, time_1h)
        data_1d = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1DAY, time_1d)

        update_db_now(symbl,"1m",data_1m,time_1m)
        update_db_now(symbl,"15m",data_15m,time_15m)
        update_db_now(symbl,"30m",data_30m,time_30m)
        update_db_now(symbl,"1h",data_1h,time_1h)
        update_db_now(symbl,"1d",data_1d,time_1d)
        
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


def update_db_now(symbl,period,data,time_frame):

    coll_name = symbl + "_" + period

    new_data = []

    if (time_frame!="25 day ago UTC"):
        data.pop(0)
    else:
        print("No collection Exists creating a new collection with 25 days of data for :" + coll_name)

    if (len(data)>0):

        for dt in data:

            new_data.append({"time":dt[0],"data":dt})

        
        db_action("insert_many",[new_data,coll_name],"admin")
    


def get_last_time(symbl,period):

    if (period in period_set) and (symbl in symbols):

        coll_name = symbl + "_" + period

        result = db_action("find_last_entry",[coll_name],"admin")

        if (result==[None]):
            return("25 day ago UTC")
        else:
            return(int(result[0]['time']))
    
    else:

        return("Invalid Period or Symbol")

def validity_check(name,interval):
    if name in symbols and interval in period_set:
        return(True)
    else:
        return(False)

        


############################################################################ Initiation Logic Ends

        
    