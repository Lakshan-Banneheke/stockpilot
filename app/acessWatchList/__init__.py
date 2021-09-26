from flask import Blueprint, request
import json
from watchList import add_stock_to_watch_list,view_watch_list,remove_from_watch_list

WLIST_BP = Blueprint('WLIST_BP', __name__)


@WLIST_BP.route('/addBrand/', methods=['POST'])
def add_to_wList():
    data = json.loads(request.data, strict=False)
    return(add_stock_to_watch_list(data['email'],data['brands']))


@WLIST_BP.route('/viewWlist/<string:email>', methods=['GET'])
def view_wList(email):
    return(view_watch_list(email))

@WLIST_BP.route('/removeBrand/', methods=['DELETE'])
def remove_from_wList():
    data = json.loads(request.data, strict=False)
    return(remove_from_watch_list(data['email'],data['brands']))

    


    




