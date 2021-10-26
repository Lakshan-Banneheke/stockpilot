from flask import make_response, jsonify

from db_access import db_action


def add_stock_to_watch_list(email, brandNames):
    current = db_action("read_one", [{"email_id": email}, "watch_list"], "admin")
    user_result = db_action("read_one", [{"email": email}, "users"], "admin")
    device_tokens = user_result['device_tokens']

    if current:
        brandList = current['brands']
        for brand in brandNames:
            if brand not in brandList:
                brandList.append(brand)
                if device_tokens:
                    token_list_result = db_action("read_one", [{"type": brand}, "notif_tokens"], "admin")
                    if token_list_result:
                        token_list = token_list_result['tokens']
                        if device_tokens not in token_list:
                            token_list = token_list + device_tokens
                        db_action("update_one", [{"type": brand}, {"$set": {"tokens": token_list}}, "notif_tokens"],
                                  "admin")
                    else:
                        token_list = device_tokens
                        db_action("insert_one", [{"type": brand, "tokens": token_list}, "notif_tokens"], "admin")


        result = db_action("update_one", [{"email_id": email}, {"$set": {"brands": brandList}}, "watch_list"], "admin")
        return make_response(jsonify({'message': "Successful", "error": False}), 200)
    else:
        result = db_action("insert_one", [{"email_id": email, "brands": brandNames}, "watch_list"], "admin")
        for brand in brandNames:
            if device_tokens:
                token_list_result = db_action("read_one", [{"type": brand}, "notif_tokens"], "admin")
                if token_list_result:
                    token_list = token_list_result['tokens']
                    if device_tokens not in token_list:
                        token_list = token_list + device_tokens
                    db_action("update_one", [{"type": brand}, {"$set": {"tokens": token_list}}, "notif_tokens"],
                              "admin")
                else:
                    token_list = device_tokens
                    db_action("insert_one", [{"type": brand, "tokens": token_list}, "notif_tokens"], "admin")
        return make_response(jsonify({'message': "Successful", "error": False}), 200)


def view_watch_list(email):
    current = db_action("read_one", [{"email_id": email}, "watch_list"], "admin")
    if current is not None:
        return make_response(jsonify({"brands": current['brands'], "error": False}), 200)
    else:
        return make_response(jsonify({"message": "Watchlist is empty", "error": True}), 200)


def remove_from_watch_list(email, brand):
    current = db_action("read_one", [{"email_id": email}, "watch_list"], "admin")
    user_result = db_action("read_one", [{"email": email}, "users"], "admin")
    device_tokens = user_result['device_tokens']

    if current:
        brandList = current['brands']

        if brand in brandList:
            brandList.remove(brand)
            if device_tokens:
                token_list_result = db_action("read_one", [{"type": brand}, "notif_tokens"], "admin")
                if token_list_result:
                    token_list = token_list_result['tokens']
                    for token in device_tokens:
                        if token in token_list:
                            token_list.remove(token)
                    db_action("update_one", [{"type": brand}, {"$set": {"tokens": token_list}}, "notif_tokens"], "admin")

        result = db_action("update_one", [{"email_id": email}, {"$set": {"brands": brandList}}, "watch_list"], "admin")
        return make_response(jsonify({'message': "Successfully updated the watch list", "error": False}), 200)
    else:
        return make_response(jsonify({'message': "No watch_list available for the given email", "error": True}), 200)
