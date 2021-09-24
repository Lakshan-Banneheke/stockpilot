from .ps_model import MessageAnnouncer

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

    
    