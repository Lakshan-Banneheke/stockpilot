from binance import ThreadedWebsocketManager
from binance.enums import KLINE_INTERVAL_15MINUTE, KLINE_INTERVAL_1DAY, KLINE_INTERVAL_1HOUR, KLINE_INTERVAL_1MINUTE, KLINE_INTERVAL_30MINUTE
from app.pubsub.data_center import announce_socket

api_key = 'sxhyNXQCWllwYdqgPIyPJ9gr5y0L8n3is23vBzpKfTdIgVIiSSX8BrTIrxm25nVV'
api_secret = '5TsvpN7ZtawCVEyV5Ts2BFlf46S7ETy8okYe9TDYJJ8VuzzoM1qvMMBOVQ7JaawW'

symbols =["BNBBTC","BNBUSDT"]


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

    



