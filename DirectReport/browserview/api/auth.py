#!/usr/bin/env python3

from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from DirectReport.models.user_model import UserModel
from DirectReport.browserview.api.errors import error_response

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

user_model = UserModel()


@basic_auth.verify_password
def verify_password(username, password):
    user = user_model.get_user_by_username(username)
    if user and user.check_password(password):
        return user


@basic_auth.error_handler
def basic_auth_error(status):
    return error_response(status)


@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)
