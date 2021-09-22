import json
from flask import Blueprint, request
from db_access import db_action


USER_BP = Blueprint('USER_BP', __name__)


@USER_BP.route('/register', methods=['POST'])
def register():
    print("REGISTER")
    data = json.loads(request.data, strict=False)
    print(data)
    result = db_action("insert_one",[{"first_name":data['user']['firstName'],"last_name":data['user']['lastName'],"email":data['user']['email']},"users"],"admin")
    print(result)
    return("Done")






