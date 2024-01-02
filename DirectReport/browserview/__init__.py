#!/usr/bin/env python3

import sys
from pathlib import Path
from flask import Flask, request
from flask import redirect, url_for
from flask_login import LoginManager, current_user
from DirectReport.browserview.services.github import GithubClient
from DirectReport.browserview.services.huggingface_client import HuggingFaceClient
from DirectReport.browserview.services.googleai_client import GoogleAIClient
from DirectReport.browserview.services.prompt_logic import generate_email
from DirectReport.config import Config
from DirectReport.datadependencies import appsecrets
from DirectReport.models.user_model import UserModel

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

client_id = appsecrets.GITHUB_CLIENT_ID
client_secret = appsecrets.GITHUB_CLIENT_SECRET
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def user_loader(email):
    user = UserModel().get_user_by_email(email)
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    user = UserModel().get_user_by_email(email)
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return redirect(url_for('auth.login'))
    else:
        if current_user.is_authenticated:
            return redirect(url_for('auth.account'))
        else:
            return redirect(url_for('auth.login'))


def create_app(config_class=Config):
    app = Flask(__name__, template_folder="templates")

    from DirectReport.browserview.auth import bp as auth_bp

    app.register_blueprint(auth_bp)

    from DirectReport.browserview.main import bp as main_bp

    app.register_blueprint(main_bp)

    from DirectReport.browserview.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix='/api')

    from DirectReport.browserview.errors import bp as errors_bp

    app.register_blueprint(errors_bp)

    from DirectReport.browserview.dashboard import bp as dashboard_bp

    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    app.secret_key = appsecrets.SECRET_KEY
    login_manager.init_app(app)
    app.config.from_object(config_class)
    return app
