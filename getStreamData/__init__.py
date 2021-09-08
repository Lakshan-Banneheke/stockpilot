from binance import ThreadedWebsocketManager


def getStreamData():

    twm = ThreadedWebsocketManager()
    # start is required to initialise its internal loop
    twm.start()

    def handle_socket_message(msg):
        # Have a switch statement for msg['s'] here which will store the relevant symbol data in the required place in the database
        print(f"message type: {msg['e']}")
        print(msg)

    twm.start_kline_socket(callback=handle_socket_message, symbol='BTCUSDT')
    twm.start_kline_socket(callback=handle_socket_message, symbol='BNBUSDT')
