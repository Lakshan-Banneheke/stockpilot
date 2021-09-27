from flask import make_response, jsonify

from db_access import db_action


def add_stock_to_watch_list(email, brandNames):
    current = db_action("read_one", [{"email_id": email}, "watch_list"], "admin")

    if current:
        brandList = current['brands']
        for brand in brandNames:
            if brand not in brandList:
                brandList.append(brand)

        result = db_action("update_one", [{"email_id": email}, {"$set": {"brands": brandList}}, "watch_list"], "admin")
        return make_response(jsonify({'message': "Successful", "error": False}), 200)
    else:
        result = db_action("insert_one", [{"email_id": email, "brands": brandNames}, "watch_list"], "admin")
        return make_response(jsonify({'message': "Successful", "error": False}), 200)


def view_watch_list(email):
    current = db_action("read_one", [{"email_id": email}, "watch_list"], "admin")
    return make_response(jsonify({"brands": current['brands'], "error": False}), 200)


def remove_from_watch_list(email, brandNames):
    current = db_action("read_one", [{"email_id": email}, "watch_list"], "admin")

    if current:
        brandList = current['brands']
        for brand in brandNames:
            if brand in brandList:
                brandList.remove(brand)

        result = db_action("update_one", [{"email_id": email}, {"$set": {"brands": brandList}}, "watch_list"], "admin")
        return make_response(jsonify({'message': "Successfully updated the watch list", "error": False}), 200)
    else:
        return make_response(jsonify({'message': "No watch_list available for the given email", "error": True}), 200)
