from typing import List
from app.pubsub.ps_model import MessageAnnouncer

def test_history_getter():
    m_announcer = MessageAnnouncer()
    response = m_announcer.get_historical_data("BNBUSDT","1m","1634947200000","1635465600000")
    assert isinstance(response,List)
