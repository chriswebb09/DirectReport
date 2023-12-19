#!/usr/bin/env python3

import sys
import os
from pathlib import Path
import urllib
import requests

from flask import Flask, render_template, session, request, redirect, json, url_for
from flask import make_response
from flask_login import LoginManager, login_required, current_user

from DirectReport.browserview.services.github import GithubClient
from DirectReport.browserview.services.prompt_logic import generate_email
from DirectReport.datadependencies import appsecrets
from DirectReport.models.user_model import UserModel
from DirectReport.browserview.blueprints.auth.auth import auth
from DirectReport.browserview.blueprints.reports.reportbp import reportsbp

file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

login_manager = LoginManager()
app = Flask(__name__, template_folder="templates")
app.register_blueprint(auth)
app.register_blueprint(reportsbp)
app.secret_key = appsecrets.SECRET_KEY

client_id = appsecrets.GITHUB_CLIENT_ID
client_secret = appsecrets.GITHUB_CLIENT_SECRET
global HEADER_TOKEN
HEADER_TOKEN = ""

headers3 = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer ' + HEADER_TOKEN,
    'X-GitHub-Api-Version': '2022-11-28'
}

app.config['OAUTH2_PROVIDERS'] = {
    'github': {
        'client_id': appsecrets.GITHUB_CLIENT_ID,
        'client_secret': appsecrets.GITHUB_CLIENT_SECRET,
        'authorize_url': 'https://github.com/login/oauth/authorize',
        'token_url': 'https://github.com/login/oauth/access_token',
        'userinfo': {
            'url': 'https://api.github.com/user/emails',
            'email': lambda json: json[0]['email'],
        },
        'scopes': ['user:email'],
    },
}
login_manager.init_app(app)
login_manager.login_view = "login"
user_model = UserModel()


@app.route('/authorize/github')
def oauth2_authorize():
    github_url = "https://github.com/login/oauth/authorize?scope=user:email&client_id=" + client_id + "&client_secret=" + client_secret + "&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcallback%2Fgithub"
    return redirect(github_url)


@app.route('/repo', methods=['GET', 'POST'])
def reponame():
    args_url = request.args.get('repo_url')
    h_token = session['header_token']
    reponame = "https://api.github.com/repos/" + args_url + "/commits"
    print(reponame)
    headers443 = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer ' + h_token,
        'X-GitHub-Api-Version': '2022-11-28'
    }
    response3 = requests.get(
        url=reponame,
        headers=headers443,
        auth=(client_id, client_secret)
    )
    json_Data3 = json.loads(response3.content)
    return json_Data3, 200

@app.route('/callback/github', methods=['GET', 'POST'])
def ouath2_callback():
    data = {'client_id': client_id, 'client_secret': client_secret, 'code': request.args.get("code")}
    response = requests.post('https://github.com/login/oauth/access_token', data=data)
    res = response.text.split('&', 1)
    token = res[0].split('=')[1]
    HEADER_TOKEN = token
    session['header_token'] = token
    headers2 = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    HEADER_TOKEN = token
    data2 = '{\n' + '  "access_token": "' + HEADER_TOKEN + '" \n}'
    response2 = requests.post(
        url="https://api.github.com/applications/" + client_id + "/token",
        headers=headers2,
        data=data2,
        auth=(client_id, client_secret),
    )
    json_Data = json.loads(response2.content)
    repos = requests.get(json_Data["user"]['repos_url'] + "?sort=updated&direction=desc", data=data2, auth=(client_id, client_secret))
    json_Data2 = json.loads(repos.content)
    results = []
    for repo in json_Data2:
        owner = repo['owner']
        url_repo = "https://api.github.com/repos/" + owner['login'] + "/" + repo['name']

        data_res = {
            "name": repo['name'],
            "description": repo['description'],
            "url": repo['url'],
            'url_repo': url_repo,
            "owner_url": owner['url']
        }
        results.append(data_res)
    return render_template('team/teamreport.html', title='Team', data=results)

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
    return render_template('team/team.html', title='Team', data=repo)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
