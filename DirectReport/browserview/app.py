#!/usr/bin/env python3

import sys
from pathlib import Path

from flask import Flask, render_template, request, redirect, json, url_for
from flask_login import LoginManager, login_required, current_user

from DirectReport.browserview.github import GithubClient
from DirectReport.browserview.prompt_logic import generate_email
from DirectReport.datadependencies import appsecrets
from DirectReport.models.user_model import UserModel
from .auth.auth import auth
from .reportbp import reportsbp

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

login_manager = LoginManager()
app = Flask(__name__, template_folder="templates")
app.register_blueprint(auth)
app.register_blueprint(reportsbp)
app.secret_key = appsecrets.SECRET_KEY
login_manager.init_app(app)
login_manager.login_view = "login"
user_model = UserModel()


@app.route("/")
def home():
    """
    Renders the homepage of the web application.
    :return: Rendered HTML template for the homepage.
    """
    return render_template('index.html', title='Home')


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors (page not found).

    :param e: The error object.
    :return: Rendered HTML template for the 404 error page.
    """
    return render_template('404.html', error=e), 404


@login_manager.user_loader
def user_loader(email):
    user = user_model.get_user_by_email(email)
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    user = user_model.get_user_by_email(email)
    return user


@app.route("/new", methods=['GET', 'POST'])
@login_required
def new():
    """
    Retrieves and renders the list of all entries.
    :return: Rendered HTML template for the list page.
    """
    return render_template('list.html', title='New Entry', data=[])


@login_manager.unauthorized_handler
def unauthorized_handler():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return redirect(url_for('auth.login'))
    else:
        if current_user.is_authenticated:
            return redirect(url_for('auth.account'))
        else:
            return redirect(url_for('auth.login'))


@app.route("/team", methods=['GET'])
def team():
    return render_template('team/team.html', title='Team', data=[])


@app.route("/generate_email", methods=['POST'])
def generateemail():
    prompt = ""
    if request.method == "POST":
        prompt = json.dumps(request.get_json()["prompt"])
    report = generate_email(prompt)
    elements = {"email": report.choices[0].message.content}
    return elements, 201


@app.route("/repo/<reponame>", methods=['GET'])
def repo(reponame=None):
    client = GithubClient()
    repo = client.get_repo_issues("chriswebb09", reponame)
    print(repo)
    return render_template('team/team.html', title='Team', data=[])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
