from typing import List
from app.stock.utils import get_symbol_set,get_historical_stock_data

def test_history_getter():
    response = get_symbol_set()
    size = len(response["stock_symbols"])
    assert size>0


# def test_history():
#     response = get_historical_stock_data("aapl","1d")
#     assert isinstance(response,List)

# def test_history_invalid():
#     response = get_historical_stock_data("aal","1d")
#     assert response == "Error in arguements"

