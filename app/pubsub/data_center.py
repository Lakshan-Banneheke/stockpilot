from .ps_model import MessageAnnouncer

announcer = MessageAnnouncer() # need to create announcers for each type of crypto saved in a dictionery

def announce_socket(): # use this function to announce the stream data to the respective user set
    for i in range(0,500):
        announcer.announce("Data")

def listen_socket(name): # according to the user input neeeds to listen to the relevent announcer instance
    if (name=='check'):
        return(announcer.listen())