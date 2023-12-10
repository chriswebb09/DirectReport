from flask import Blueprint
from flask import Flask, render_template, request, redirect, json, url_for
from werkzeug.security import generate_password_hash
from DirectReport.models.user_model import UserModel
from DirectReport.models.list_builder import ListBuilder
from DirectReport.browserview.prompt_logic import generate_email
from DirectReport.browserview.github import GithubClient
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from DirectReport.datadependencies import appsecrets
# from .auth.auth import auth

auth = Blueprint('auth', __name__)

# @auth.route('/signup')
# def signup():
#     pass
#
# @auth.route('/login')
# def login():
#     pass
#
# @auth.route('/logout')
# def logout():
#     pass



# from flask import Blueprint
#
# auth = Blueprint('auth', __name__)
#
# @auth.route('/login')
# def login():
#     return 'Login'
#
# @auth.route('/signup')
# def signup():
#     return 'Signup'
#
# @auth.route('/logout')
# def logout():
#     return 'Logout'