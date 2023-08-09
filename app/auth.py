# from functools import wraps
# from flask import request, abort, make_response
# import os

# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         auth_username = os.environ.get("AUTH_USERNAME")
#         auth_password = os.environ.get("DATABASE_PASSWORD")
        
#         if not auth or not check_auth(auth.username, auth.password, auth_username, auth_password):
#             return authenticate()
#         return f(*args, **kwargs)
#     return decorated

# def check_auth(username, password, expected_username, expected_password):
#     return username == expected_username and password == expected_password

# def authenticate():
#     # Return a 401 Unauthorized response
#     return abort(make_response({"error": "Authentication required"}, 401))
