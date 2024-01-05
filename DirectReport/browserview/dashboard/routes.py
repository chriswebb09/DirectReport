#!/usr/bin/env python3

import requests
from flask import render_template, session, request, redirect, json, jsonify
from flask_login import login_user, login_required, logout_user, current_user
import re
from DirectReport.browserview.dashboard import bp
from DirectReport.models.report.report_builder import ReportBuilder
from DirectReport.browserview.services.github import GithubClient
from DirectReport.browserview.services.huggingface_client import HuggingFaceClient
from DirectReport.browserview.services.googleai_client import GoogleAIClient
from DirectReport.browserview.services.prompt_logic import generate_email, team_summary_from_shortlog
from DirectReport.models.report.report_model import ReportModel
from DirectReport.datadependencies import appsecrets

client_id = appsecrets.GITHUB_CLIENT_ID
client_secret = appsecrets.GITHUB_CLIENT_SECRET


@bp.route("/home", methods=['GET', 'POST'])
@login_required
def dashboard_home():
    return render_template('account.html', title='Account', name=current_user.username, userid=current_user.id)


@bp.route("/edit", methods=['GET', 'POST'])
@login_required
def dashbboard_edit():
    return render_template('edit_account.html', title='Edit Account')


@bp.route("/reports/saved", methods=['GET', 'POST'])
@login_required
def dashboard_reports_saved():
    """
    Retrieves and renders the list of all entries.
    :return: Rendered HTML template for the list page.
    """

    results = requests.get('http://127.0.0.1:5000/api/reports/list')
    return render_template('list.html', title='List', data=results)


@bp.route("/reports/new", methods=['GET', 'POST'])
@login_required
def dashboard_reports_new():
    return render_template('team/teamreport.html', title='Team Report', data=[])


@bp.route("/reports/update", methods=['GET', 'POST'])
@login_required
def dashboard_reports_update():
    prompt = ""
    googleAi = GoogleAIClient()
    prompt = request.get_json()["prompt"].strip()
    client = GithubClient()
    h_token = session['header_token']
    user_repos = client.get_user_repos(current_user.github_username, h_token)
    commits_last_month = client.get_commits_in_last_month(current_user.github_username, current_user.github_repo, h_token)
    commits_last_sixty = client.get_commits_in_last_sixty_days(current_user.github_username, current_user.github_repo, h_token)
    commits_last_ninety = client.get_commits_in_last_ninety_days(current_user.github_username, current_user.github_repo, h_token)
    get_pull_requests_count = client.get_pull_requests_count(current_user.github_username, current_user.github_repo, h_token)
    get_pull_requests_count_sixty = client.get_pull_requests_count_sixty_days(current_user.github_username, current_user.github_repo, h_token)
    repo_data = []
    for repo in user_repos:
        repo_data.append(repo["name"])
    raw_data = team_summary_from_shortlog(prompt)
    print(raw_data)
    raw_reponse = raw_data["choices"][0]["message"]["content"]
    response_data = json.loads(raw_reponse)
    # print(response_data)
        # list(raw_data.choices)[0]
    # my_openai_obj.to_dict()['message']['content']
    # response_data = json.loads(raw_data)
    # response_data = json.dumps(raw_data)
    # raw_data = googleAi.get_data_from(prompt)
    # begin, end = raw_data.find('{'), raw_data.rfind('}')
    # filtered_str = raw_data[begin: end + 1]
    # response_data = json.loads(filtered_str)
    response_data["broad_categories"] = {
        "debug_info": 16,
        "code_maintenance": 9,
        "documentation": 7,
        "test_related": 6,
        "nonbreaking_space_handling": 5,
        "readme_update": 1,
        "syntax_fix": 1,
    }
    response_data["commit_nums"] = {"15 days": 4, "30 days": (commits_last_month / 10), "60 days": (commits_last_sixty / 10), "90 days": (commits_last_ninety / 10), "120 days": 30}
    response_data["pull_requests"] = {"30 days": 5, "60 days": 10, "90 days": 15, "120 days": 20, "150 days": 20, "1 year": 30}
    response_data["repos"] = repo_data
    ReportBuilder.new(response_data, prompt, current_user.id, "DirectReport")
    return response_data, 201


@bp.route("/reports/<uid>", methods=['GET'])
@login_required
def dashboard_saved_report(uid=None):
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    report = list(filter(lambda report: report["uuid"] == uid, reports))[0]
    json_data = json.dumps(report)
    return render_template(
        'team/teamreport.html', title='Team Report', data=json_data, report=json_data, raw_input=report['raw_input']
    )
