from binance import ThreadedWebsocketManager
from app.pubsub.data_center import announce_socket

api_key = 'sxhyNXQCWllwYdqgPIyPJ9gr5y0L8n3is23vBzpKfTdIgVIiSSX8BrTIrxm25nVV'
api_secret = '5TsvpN7ZtawCVEyV5Ts2BFlf46S7ETy8okYe9TDYJJ8VuzzoM1qvMMBOVQ7JaawW'


def getStreamData():

    twm = ThreadedWebsocketManager(api_key=api_key, api_secret=api_secret)
    # start is required to initialise its internal loop
    twm.start()

    print("Publisher started working !!!")

    def handle_socket_message(msg):
        # Have a switch statement for msg['s'] here which will store the relevant symbol data in the required place in the database
        # print(f"message type: {msg['e']}")
        announce_socket(msg['s'],msg)
        # print(msg)
        # print(msg['s'])

    twm.start_kline_socket(callback=handle_socket_message, symbol='BNBBTC')
    twm.start_kline_socket(callback=handle_socket_message, symbol='BNBUSDT')

    twm.join()

    

