from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    pass

@auth.route('/login')
def login():
    pass

@auth.route('/logout')
def logout():
    pass

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