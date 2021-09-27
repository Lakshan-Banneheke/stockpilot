from flask import Blueprint, request
import json

from app.user import token_required
from watchList import add_stock_to_watch_list,view_watch_list,remove_from_watch_list

WLIST_BP = Blueprint('WLIST_BP', __name__)


@WLIST_BP.route('/addBrand', methods=['POST'])
@token_required
def add_to_wList(current_user):
    data = json.loads(request.data, strict=False)
    print(data['brands'])
    return add_stock_to_watch_list(current_user['email'], data['brands'])


@WLIST_BP.route('/view', methods=['GET'])
@token_required
def view_wList(current_user):
    return view_watch_list(current_user['email'])

@WLIST_BP.route('/removeBrand', methods=['DELETE'])
@token_required
def remove_from_wList(current_user):
    data = json.loads(request.data, strict=False)
    return remove_from_watch_list(current_user['email'], data['brands'])

    


    




