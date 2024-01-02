#!/usr/bin/env python3

from datetime import datetime, timedelta

import requests
from flask import render_template, session, request, redirect, json, jsonify
from flask_login import current_user

from DirectReport.models.user_model import UserModel
from DirectReport.browserview.main import bp
from DirectReport.browserview.services.github import GithubClient
from DirectReport.browserview.services.prompt_logic import generate_email
from DirectReport.datadependencies import appsecrets

client_id = appsecrets.GITHUB_CLIENT_ID
client_secret = appsecrets.GITHUB_CLIENT_SECRET


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        print("authenticated user")
    else:
        print("unauthenticated user")


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


def get_commits_last_month(repo_name):
    owner = current_user.github_username
    url = f'https://api.github.com/repos/{owner}/{repo_name}/pulls'
    h_token = session['header_token']
    headers = {"Authorization": f"token {h_token}"}
    since_date = (datetime.utcnow() - timedelta(days=30)).strftime('%Y-%m-%dT%H:%M:%SZ')
    params = {'state': 'all', 'sort': 'created', 'direction': 'desc', 'since': since_date}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        pull_requests = response.json()
        print(pull_requests)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

@bp.route('/repo', methods=['GET', 'POST'])
def reponame():
    print("\n")
    print(request.method)
    print("/repo")
    args_url = request.args.get('repo_url')
    print(args_url)
    h_token = session['header_token']
    repo_name = "https://api.github.com/repos/" + args_url + "/commits"
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer ' + h_token,
        'X-GitHub-Api-Version': '2022-11-28',
    }
    response_data = requests.get(url=repo_name, headers=headers, auth=(client_id, client_secret))
    if response_data.status_code == 200:
        json_response_data = json.loads(response_data.content)
        res_json = {"json_array": json_response_data}
        return res_json, 200
    else:
        return jsonify([]), 200


@bp.route('/callback/github', methods=['GET', 'POST'])
def ouath2_callback():
    print("/callback/github")
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
    data2 = '{\n' + '  "access_token": "' + HEADER_TOKEN + '" \n}'
    response2 = requests.post(
        url="https://api.github.com/applications/" + client_id + "/token",
        headers=headers2,
        data=data2,
        auth=(client_id, client_secret),
    )
    json_Data = json.loads(response2.content)
    user_info = json_Data["user"]
    user_model = UserModel()
    user_model.update_github_username(current_user.email, user_info["login"])
    return render_template('team/teamreport.html', title='Team', data=[])


@bp.route('/repos', methods=['GET', 'POST'])
def repos():
    print("\n")
    print(request.method)
    print("/repos")
    if request.method == 'GET':
        h_token = session['header_token']
        username = current_user.github_username
        url = f"https://api.github.com/users/{username}/repos" + "?sort=updated&direction=desc"
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer ' + h_token,
            'X-GitHub-Api-Version': '2022-11-28',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repos = response.json()
            results = []
            for repo in repos:
                owner = repo['owner']
                url_repo = repo['url']
                data_res = {
                    "name": repo['name'],
                    "description": repo['description'],
                    "url": repo['url'],
                    'url_repo': url_repo,
                    "owner_url": owner['url'],
                }
                results.append(data_res)
            return jsonify(results), 200
        else:
            print(f"Error Response FROM API: {response.status_code} - {response.text}")
            return jsonify([]), 200
    else:
        print("posted to repos")
        return jsonify([]), 200



@bp.route("/team", methods=['GET'])
def team():
    return render_template('team/team.html', title='Team', data=[])


@bp.route("/generate_email", methods=['POST'])
def generateemail():
    prompt = ""
    if request.method == "POST":
        prompt = json.dumps(request.get_json()["prompt"])
    report = generate_email(prompt)
    elements = {"email": report.choices[0].message.content}
    return elements, 201


@bp.route("/repo/<reponame>", methods=['GET'])
def repo(reponame=None):
    client = GithubClient()
    try:
        repo = client.get_repo_issues(current_user.github_username, reponame)
        print(repo)
        print("\n")
    except Exception as e:
        print(e)
        repo = []
    return render_template('team/team.html', title='Team', data=repo)
