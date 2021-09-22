import json
import os
import uuid
from functools import wraps

import jwt
from flask import Blueprint, render_template, request, make_response, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta

import app
from db_access import db_action, read_one_from_collection

USER_BP = Blueprint('USER_BP', __name__)


#
# # decorator for verifying the JWT
# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None
#
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']
#
#         if not token:
#             return jsonify({'message': 'Token is missing !'}), 401
#
#         try:
#             data = jwt.decode(token, os.environ['SECRET_KEY'])
#             # current_user = get user
#         except:
#             return jsonify({'message': 'Token is invalid !'}), 401
#
#         return f(current_user, *args, **kwargs)
#
#     return decorated
#
#
# @USER_BP.route('/login', methods=['POST'])
# def login():
#     auth = json.loads(request.data, strict=False)
#
#     if not auth or not auth['email'] or not auth['password']:
#         return make_response(jsonify({'message': 'All fields are required for logging in'}), 400)
#
#     # user = get user from db
#
#     if not user:
#         return make_response(jsonify({'message': 'Wrong Username or Password'}), 401)
#
#     if not check_password_hash(user.password, auth['password']):
#         return make_response(jsonify({'message': 'Wrong Username or Password'}), 401)
#
#     else:
#         try:
#             token = jwt.encode({
#                 'public_id': user.public_id,
#                 'exp': datetime.utcnow() + timedelta(minutes=30)
#             }, os.environ['SECRET_KEY'])
#             return make_response(jsonify({'token': token.decode('UTF-8')}), 201)
#
#         except:
#             return make_response(jsonify({'message': 'Login Failed'}), 401)


@USER_BP.route('/register', methods=['POST'])
def register():
    print("register")

    data = json.loads(request.data, strict=False)
    print(data)
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    password = data['password']

    # if password != repass:
    #     return make_response(jsonify({'message': 'Passwords Do Not Match'}), 400)

    user_email = db_action("read_one", [{"email": email}, "users"], "general")

    if user_email:
        return make_response(jsonify({'message': 'Email already inuse.'}), 400)


    else:
        try:
            new_user = {
                "public_id": str(uuid.uuid4()),
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "password": generate_password_hash(password, method='sha256'),
            }

            db_action("insert_one", [new_user, "users"], "general")
            return make_response(jsonify({'message': 'Successfully registered.'}), 201)

        except:
            return make_response(jsonify({'message': 'Registration Failed.'}), 500)

