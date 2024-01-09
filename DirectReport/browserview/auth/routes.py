#!/usr/bin/env python3

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash
from DirectReport.browserview.auth import bp
from DirectReport.datadependencies import appsecrets
from DirectReport.models.user_model import UserModel


user_model = UserModel()


@bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # code to validate and add user to database goes here
        email = request.form.get('email')
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password_text = request.form.get('password')
        password = generate_password_hash(password_text)
        user_model.insert_user(email, username, firstname, lastname, email, password)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = user_model.get_user_by_email(email)
        if user and user.check_password(password):
            login_user(user, remember=remember, force=True)
            if current_user.is_authenticated():
                return redirect(url_for('dashboard.dashboard_home'))
        else:
            flash("Please check your login details and try again.")
    return render_template(
        'auth/login.html', client_id=appsecrets.GITHUB_CLIENT_ID, client_secret=appsecrets.GITHUB_CLIENT_SECRET
    )
