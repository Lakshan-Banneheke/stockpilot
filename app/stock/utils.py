from db_access import db_action


def get_symbol_set():
    symbl_set = db_action("read_one", [{"type": "stock"}, "symbols"], "admin")
    dt = symbl_set['data']
    return {"stock_symbols": dt}


def get_historical_stock_data(symbl, interval):
    interval_modified = "data_" + interval
    hist = db_action("read_one", [{"type": interval_modified}, symbl], "admin")
    
    if (hist):
        return hist['data']
    else:
        return ("Error in arguements")



