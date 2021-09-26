from db_access import db_action
from binance import ThreadedWebsocketManager
from binance.enums import KLINE_INTERVAL_15MINUTE, KLINE_INTERVAL_1DAY, KLINE_INTERVAL_1HOUR, KLINE_INTERVAL_1MINUTE, KLINE_INTERVAL_30MINUTE
from app.pubsub.data_center import announce_socket

api_key = 'sxhyNXQCWllwYdqgPIyPJ9gr5y0L8n3is23vBzpKfTdIgVIiSSX8BrTIrxm25nVV'
api_secret = '5TsvpN7ZtawCVEyV5Ts2BFlf46S7ETy8okYe9TDYJJ8VuzzoM1qvMMBOVQ7JaawW'

symbols =[]


def getStreamData():

    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)

    twm.start()

    print("Publisher started working !!!")

    for smbl in symbols:
        start_to_listen(twm,smbl)
    
    twm.join()

    

def start_to_listen(twm,symbl):

    def handle_socket_message(msg):
        announce_socket(msg['s'],msg['k']['i'],msg)
        print(msg['s'],msg['k']['i'])

    twm.start_kline_socket(callback=handle_socket_message, symbol=symbl, interval=KLINE_INTERVAL_1MINUTE)
    twm.start_kline_socket(callback=handle_socket_message, symbol=symbl, interval=KLINE_INTERVAL_15MINUTE)
    twm.start_kline_socket(callback=handle_socket_message, symbol=symbl, interval=KLINE_INTERVAL_30MINUTE)
    twm.start_kline_socket(callback=handle_socket_message, symbol=symbl, interval=KLINE_INTERVAL_1HOUR)
    twm.start_kline_socket(callback=handle_socket_message, symbol=symbl, interval=KLINE_INTERVAL_1DAY)

def get_symbol_set():

    symbl_set = db_action("read_one",[{"type":"crypto"},"symbols"],"admin")

    dt = symbl_set['data']

    return({"crypto_symbols":dt})

def update_symbol_set(name):

    symbl_set = db_action("read_one",[{"type":"crypto"},"symbols"],"admin")

    new_data = symbl_set['data']

    if (symbl_set):
        new_data.append(name)
        db_action("update_one",[{"type":"crypto"},{"$set":{"data":new_data}},"symbols"],"admin")
        update_in_memory()

        return("Successfully updated")
    else:
        return("data base error")

def update_in_memory():

    symbl_set = db_action("read_one",[{"type":"crypto"},"symbols"],"admin")

    for symbl in symbl_set['data']:

        if (symbl not in symbols):

            symbols.append(symbl)
    
    print(symbols)







    



