from .ps_model import MessageAnnouncer
from binance.client import Client
from app.utils.db_access import db_action
from time import time


announcers = {}

symbols = []

reverse_date = {"1m":1,"15m":5,"30m":10,"1h":15,"1d":150}

period_set = ["1m","15m","30m","1h","1d"]


############################################################################ Functions related to the live listening of Crypto data Starts

def announce_socket(name,interval,raw_data): # use this function to announce the stream data to the respective user set
    try:
        announcers[name][interval].announce(raw_data)
    except:
        print("Error in announcing")


def listen_socket(name,interval): # according to the user input neeeds to listen to the relevent announcer instance
    try:
        announcer = announcers[name][interval]
        return(announcer.listen())
    except:
        return("Socket doesnt respond")


def get_history(symbl,interval,s_date):


    try:
        if (s_date == "0000"):
            s_date = round(time() * 1000)
        e_date = int(round(float(s_date))) - (reverse_date[interval]*24*60*60*1000)
        return(announcers[symbl][interval].get_historical_data(symbl,interval,int(round(float(s_date))),int(e_date)))
    except:
        return("Get_history @data center faileds")
        

############################################################################ Functions related to the live listening of Crypto data Ends

############################################################################ Initiation Logic Starts

def initiate_publisher_set():

    try:
        for symbl in symbols:
            announcers[symbl] = {"1d":MessageAnnouncer(),"1h":MessageAnnouncer(),"30m":MessageAnnouncer(),"15m":MessageAnnouncer(),"1m":MessageAnnouncer()}
    except:
        print("Error in initiate_publisher_set")

def initiate_historical_data_set():

    try:

        client = Client()

        for symbl in symbols:

            time_1m = get_last_time(symbl,"1m")
            time_15m = get_last_time(symbl,"15m")
            time_30m = get_last_time(symbl,"30m")
            time_1h = get_last_time(symbl,"1h")
            time_1d = get_last_time(symbl,"1d")

            if time_1m != "Error":
                data_1m = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1MINUTE, time_1m)
            if time_15m != "Error":
                data_15m = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_15MINUTE, time_15m)
            if time_30m != "Error":
                data_30m = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_30MINUTE, time_30m)
            if time_1h != "Error":
                data_1h = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1HOUR, time_1h)
            if time_1d != "Error":
                data_1d = client.get_historical_klines(symbl, Client.KLINE_INTERVAL_1DAY, time_1d)

            update_db_now(symbl,"1m",data_1m,time_1m)
            update_db_now(symbl,"15m",data_15m,time_15m)
            update_db_now(symbl,"30m",data_30m,time_30m)
            update_db_now(symbl,"1h",data_1h,time_1h)
            update_db_now(symbl,"1d",data_1d,time_1d)

            print("History Set For:",symbl)

    except:
        print("Cannot Set Historical Data")

    
def initiate_in_memory():

    try:

        symbl_set = db_action("read_one",[{"type":"crypto"},"symbols"],"admin")

        if symbl_set != "Error":

            for symbl in symbl_set['data']:

                if (symbl not in symbols):

                    symbols.append(symbl)
    except:

        print("Error in initiate_in_memory")
    


def initiate_pub_sub():

    try:

        initiate_in_memory()
        initiate_publisher_set()
        # initiate_historical_data_set()

        print("PubSub Initiated",symbols)
    
    except:

        print("Cannot start the server")


def update_db_now(symbl,period,data,time_frame):

    try:
        coll_name = symbl + "_" + period

        new_data = []

        if (time_frame!="250 day ago UTC"):
            data.pop(0)
        else:
            print("No collection Exists creating a new collection with 250 days of data for :" + coll_name)

        if (len(data)>0):

            for dt in data:

                new_data.append({"time":dt[0],"data":dt})

            
            db_action("insert_many",[new_data,coll_name],"admin")
    except:
        print("Couldnt Set History for",coll_name)
    


def get_last_time(symbl,period):

    if (period in period_set) and (symbl in symbols):

        coll_name = symbl + "_" + period

        result = db_action("find_last_entry",[coll_name],"admin")

        if result != "Error":

            if (result==[None]):
                return("250 day ago UTC")
            else:
                return(int(result[0]['time']))

        else:

            return("Error")
    
    else:

        return("Error")

def validity_check(name,interval):
    if name in symbols and interval in period_set:
        return(True)
    else:
        return(False)

        


############################################################################ Initiation Logic Ends

        
    