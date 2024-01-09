#!/usr/bin/env python3

import requests
from flask import render_template, session, request, redirect, json, jsonify
from flask_login import current_user
from DirectReport.models.user_model import UserModel
from DirectReport.browserview.main import bp
from DirectReport.browserview.services.github import GithubClient
from DirectReport.datadependencies import appsecrets


client_id = appsecrets.GITHUB_CLIENT_ID
client_secret = appsecrets.GITHUB_CLIENT_SECRET


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        pass
    else:
        pass


@bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html', title='Home')


@bp.route('/authorize/github')
def oauth2_authorize():
    github_url = (
        "https://github.com/login/oauth/authorize?scope=user:email&client_id="
        + client_id
        + "&client_secret="
        + client_secret
        + "&redirect_uri=http%3A%2F%2F127.0.0.1%3A5000%2Fcallback%2Fgithub"
    )
    return redirect(github_url)


@bp.route('/callback/github', methods=['GET', 'POST'])
def ouath2_callback():
    data = {'client_id': client_id, 'client_secret': client_secret, 'code': request.args.get("code")}
    response = requests.post('https://github.com/login/oauth/access_token', data=data)
    res = response.text.split('&', 1)
    token = res[0].split('=')[1]
    session['header_token'] = token
    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    access_token = '{\n' + '  "access_token": "' + token + '" \n}'
    response2 = requests.post(
        url="https://api.github.com/applications/" + client_id + "/token",
        headers=headers,
        data=access_token,
        auth=(client_id, client_secret),
    )
    json_data = json.loads(response2.content)
    user_info = json_data["user"]
    user_model = UserModel()
    user_model.update_github_username(current_user.email, user_info["login"])
    return render_template('team/teamreport.html', title='Team', data=[])


@bp.route("/team", methods=['GET'])
def team():
    return render_template('team/team.html', title='Team', data=[])


@bp.route("/repo/<reponame>", methods=['GET'])
def repo(reponame=None):
    client = GithubClient()
    repo = []
    try:
        repo = client.get_repo_issues(current_user.github_username, reponame)
    except Exception as e:
        print(e)
    return render_template('team/team.html', title='Team', data=repo)
