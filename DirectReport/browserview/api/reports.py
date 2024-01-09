#!/usr/bin/env python3

from datetime import datetime, timedelta
import requests
from flask import session, request, json, jsonify
from flask_login import login_required, current_user
from DirectReport.models.user_model import UserModel
from DirectReport.models.report.report_builder import ReportBuilder
from DirectReport.browserview.services.prompt_logic import generate_email, team_summary_from_shortlog
from DirectReport.browserview.services.github import GithubClient
from DirectReport.browserview.api import bp
from DirectReport.datadependencies import appsecrets

client_id = appsecrets.GITHUB_CLIENT_ID
client_secret = appsecrets.GITHUB_CLIENT_SECRET


@bp.route("/reports/list", methods=['GET'])
@login_required
def get_list():
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    return reports, 201


@bp.route("/reports/update", methods=['GET', 'POST'])
@login_required
def dashboard_reports_update():
    prompt = ""
    prompt = request.get_json()["prompt"].strip()
    client = GithubClient()
    h_token = session['header_token']
    user_repos = client.get_user_repos(current_user.github_username, h_token)
    commits_count_last_month = client.get_commits_count_in_last_month(
        current_user.github_username, current_user.github_repo, h_token
    )
    commits_count_last_sixty = client.get_commits_count_in_last_sixty_days(
        current_user.github_username, current_user.github_repo, h_token
    )
    commits_count_last_ninety = client.get_commits_count_in_last_ninety_days(
        current_user.github_username, current_user.github_repo, h_token
    )

    get_pull_requests_count = client.get_pull_requests_count(
        current_user.github_username, current_user.github_repo, h_token
    )
    get_pull_requests_count_sixty = client.get_pull_requests_count_sixty_days(
        current_user.github_username, current_user.github_repo, h_token
    )
    repo_data = []
    for repo in user_repos:
        repo_data.append(repo["name"])
    raw_data = team_summary_from_shortlog(prompt)["choices"][0]["message"]["content"]
    response_data = json.loads(raw_data)
    response_data["commit_nums"] = {
        "15 days": 4,
        "30 days": (commits_count_last_month / 10),
        "60 days": (commits_count_last_sixty / 10),
        "90 days": (commits_count_last_ninety / 10),
        "120 days": 10,
    }
    response_data["pull_requests"] = {
        "30 days": get_pull_requests_count,
        "60 days": get_pull_requests_count_sixty,
        "90 days": 8,
        "120 days": 10,
        "150 days": 10,
        "1 year": 30,
    }
    response_data["repos"] = repo_data
    print(response_data)
    ReportBuilder.new(response_data, prompt, current_user.id, current_user.github_repo)
    return response_data, 201


@bp.route('/repo', methods=['GET', 'POST'])
def reponame():
    args_url = request.args.get('repo_url')
    repo = args_url.split('/')[1]
    h_token = session['header_token']
    client = GithubClient()
    user_model = UserModel()
    user_model.update_github_repo(current_user.email, repo)
    test = client.get_commits_in_last_month(current_user.github_username, current_user.github_repo, h_token)
    json_response_data = json.dumps(test)
    json_response_data_loads = json.loads(json_response_data)
    res_json = {"json_array": json_response_data_loads}
    return res_json, 200


@bp.route('/repos', methods=['GET', 'POST'])
def repos():
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
        return jsonify([]), 200


@bp.route("/generate_email", methods=['POST'])
def generateemail():
    prompt = ""
    if request.method == "POST":
        prompt = json.dumps(request.get_json()["prompt"])
    report = generate_email(prompt)
    elements = {"email": report.choices[0].message.content}
    return elements, 201
