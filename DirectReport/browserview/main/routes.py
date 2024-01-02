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
    print(current_user)


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


def get_commits_last_month():
    owner = 'chriswebb09'
    repo = 'your_repository'
    url = f'https://api.github.com/repos/{owner}/{repo}/pulls'
    # Replace 'your_token' with your personal access token
    headers = {'Authorization': 'token your_token'}
    # Calculate the date one month ago
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
    args_url = request.args.get('repo_url')
    h_token = session['header_token']
    reponame = "https://api.github.com/repos/" + args_url + "/commits"
    headers443 = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer ' + h_token,
        'X-GitHub-Api-Version': '2022-11-28',
    }
    response3 = requests.get(url=reponame, headers=headers443, auth=(client_id, client_secret))
    json_Data3 = json.loads(response3.content)

    USERNAME = current_user.github_username
    REPO = "DirectReport"

    # Calculate the date one month ago
    last_month = datetime.utcnow() - timedelta(days=30)
    last_month_str = last_month.strftime("%Y-%m-%dT%H:%M:%SZ")

    # API endpoint to retrieve commits for a repository since the last month
    api_url = f"https://api.github.com/repos/{USERNAME}/{REPO}/commits?since={last_month_str}"

    # Fetch commits using requests and your GitHub token
    headers = {"Authorization": f"token {appsecrets.GITHUB_TOKEN}"}
    response = requests.get(api_url, headers=headers)

    # Check if the request was successful (status code 200)
    results_2 = []
    if response.status_code == 200:
        commits = response.json()

        # Format and print the commits
        for commit in commits:
            author_name = commit["commit"]["author"]["name"]
            commit_message = commit["commit"]["message"]
            results_2.append(f"{author_name}: {commit_message}")
    else:
        print(f"Error: {response.status_code} - {response.text}")
    results = []
    for commit in json_Data3:
        commit_data_res = {
            "message": commit["commit"]["message"],
            "url": commit["commit"]["url"],
            "commit_author_name": commit["commit"]["author"]["name"],
            "commit_author_email": commit["commit"]["author"]["email"],
            "commit_author_date": commit["commit"]["author"]["date"],
            "committer_name": commit["commit"]["committer"]["name"],
            "committer_email": commit["commit"]["committer"]["email"],
            "committer_date": commit["commit"]["committer"]["date"],
            "comment_count": commit["commit"]["comment_count"],
            "verified": commit["commit"]["verification"]["verified"],
            "verification_reason": commit["commit"]["verification"]["reason"],
            "verification_signature": commit["commit"]["verification"]["signature"],
            "type": "commit",
        }
        results.append(commit_data_res)
    result_log = " ".join(results_2)
    res_json = {"json_array": json_Data3, "result_log": result_log}
    print(result_log)
    return res_json, 200


@bp.route('/callback/github', methods=['GET', 'POST'])
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
    # args_url = request.args.get('repo_url')
    h_token = session['header_token']
    username = current_user.github_username  # Replace with the GitHub username
    url = f"https://api.github.com/users/{username}/repos" + "?sort=updated&direction=desc"
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer ' + h_token,
        'X-GitHub-Api-Version': '2022-11-28',
    }
    response = requests.get(url, headers=headers)
    repos = response.json()
    results = []
    for repo in repos:
        owner = repo['owner']
        url_repo = "https://api.github.com/repos/" + owner['login'] + "/" + repo['name']
        data_res = {
            "name": repo['name'],
            "description": repo['description'],
            "url": repo['url'],
            'url_repo': url_repo,
            "owner_url": owner['url'],
        }
        results.append(data_res)
    return jsonify(results), 200

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
    repo = client.get_repo_issues(current_user.github_username, reponame)
    return render_template('team/team.html', title='Team', data=repo)
