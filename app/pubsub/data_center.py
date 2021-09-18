from .ps_model import MessageAnnouncer

announcers = {"BNBBTC":MessageAnnouncer(),"BNBUSDT":MessageAnnouncer()}

def announce_socket(name,raw_data): # use this function to announce the stream data to the respective user set
    announcers[name].announce(raw_data)

def listen_socket(name): # according to the user input neeeds to listen to the relevent announcer instance
    if (name=='BNBBTC'):
        announcer = announcers['BNBBTC']
        return(announcer.listen())

    elif (name=='BNBUSDT'):
        announcer = announcers['BNBUSDT']
        return(announcer.listen())
    
    