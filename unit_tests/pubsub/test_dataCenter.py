from app.pubsub.data_center import get_last_time,initiate_in_memory


def test_invalid_symbol():
    initiate_in_memory()
    response = get_last_time("BNBUSD","1m")
    assert response == "Error"

def test_invalid_period():
    initiate_in_memory
    response = get_last_time("BNBUSDT","156m")
    assert response == "Error"

def test_invalid_p_or_s():
    initiate_in_memory
    response = get_last_time("BNBUST","156m")
    assert response == "Error"


def test_valid_entry():
    initiate_in_memory
    response = get_last_time("BNBUSDT","15m")
    assert isinstance(response,int)