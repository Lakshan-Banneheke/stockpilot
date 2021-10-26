import json
from flask import Blueprint, request
from db_access import db_action
import os
import uuid
from functools import wraps

import jwt
from flask import Blueprint, request, make_response, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta

from db_access import db_action

USER_BP = Blueprint('USER_BP', __name__)


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, os.environ['SECRET_KEY'], algorithms=["HS256"])
            current_user = db_action("read_one", [{"public_id": data['public_id']}, "users"], "admin")
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


@USER_BP.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data, strict=False)
    user = data['creds']
    try:
        if not user or not user['email'] or not user['password']:
            return make_response(jsonify({'message': 'All fields are required for logging in'}), 200)
    except:
        return make_response(jsonify({'message': 'All fields are required for logging in'}), 200)

    user_data = db_action("read_one", [{"email": user['email']}, "users"], "admin");
    if not user_data:
        return make_response(jsonify({'message': 'Wrong Username or Password'}), 200)

    if not check_password_hash(user_data['password'], user['password']):
        return make_response(jsonify({'message': 'Wrong Username or Password'}), 200)

    else:
        try:
            del user_data['_id']
            token = jwt.encode({
                "public_id": user_data['public_id'],
                "user_data": user_data,
                "exp": datetime.utcnow() + timedelta(minutes=3000)
            }, os.environ['SECRET_KEY'])
            return make_response(jsonify({'token': token, 'message': 'Login Successful!'}), 200)

        except:
            return make_response(jsonify({'message': 'Login Failed'}), 200)


@USER_BP.route('/register', methods=['POST'])
def register():
    data = json.loads(request.data, strict=False)
    first_name = data['user']['firstName']
    last_name = data['user']['lastName']
    email = data['user']['email']
    password = data['user']['password']

    # if password != repass:
    #     return make_response(jsonify({'message': 'Passwords Do Not Match'}), 400)

    user_email = db_action("read_one", [{"email": email}, "users"], "admin")

    if user_email:
        return make_response(jsonify({'message': 'Email already inuse.'}), 200)

    else:
        try:
            new_user = {
                "public_id": str(uuid.uuid4()),
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "password": generate_password_hash(password, method='sha256'),
                "device_tokens" : [],
            }

            db_action("insert_one", [new_user, "users"], "admin")
            return make_response(jsonify({'message': 'Successfully Registered'}), 201)
        except:
            return make_response(jsonify({'message': 'Database Error'}), 200)


# test route
@USER_BP.route('/test', methods=['GET'])
@token_required
def get_test(current_user):
    print(current_user)
    return make_response(jsonify({'message': 'OK'}), 200)



