
from db_access import db_action


def add_stock_to_watch_list(email,brandNames):
    
    current = db_action("read_one",[{"email_id":email},"watch_list"],"admin")

    if(current):
        brandList = current['brands']
        for brand in brandNames:
            if brand not in brandList:
                brandList.append(brand)

        result = db_action("update_one",[{"email_id":email},{"$set":{"brands":brandList}},"watch_list"],"admin")
        return("successfully updated the watch list")
    else:
        result = db_action("insert_one",[{"email_id":email,"brands":brandNames},"watch_list"],"admin")
        return("Successfully created a new watch_list and entered the brand")

def view_watch_list(email):
    
    print(email)

    current = db_action("read_one",[{"email_id":email},"watch_list"],"admin")

    print(current)

    return({"brands":current['brands']})

def remove_from_watch_list(email,brandNames):

    current = db_action("read_one",[{"email_id":email},"watch_list"],"admin")

    if(current):
        brandList = current['brands']
        for brand in brandNames:
            if brand in brandList:
                brandList.remove(brand)

        result = db_action("update_one",[{"email_id":email},{"$set":{"brands":brandList}},"watch_list"],"admin")
        return("successfully updated the watch list")
    else:
        return("No watch_list available for the given email")
