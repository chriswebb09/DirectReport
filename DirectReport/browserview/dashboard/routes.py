#!/usr/bin/env python3

import requests
from flask import render_template
from flask_login import login_required, current_user
from DirectReport.browserview.dashboard import bp
from DirectReport.models.report.report_builder import ReportBuilder
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


@bp.route("/reports/<uid>", methods=['GET'])
@login_required
def dashboard_saved_report(uid=None):
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    report = list(filter(lambda report: report["uuid"] == uid, reports))[0]
    report["commit_nums"] = {
        "15 days": 4,
        "30 days": (8 / 10),
        "60 days": (10 / 10),
        "90 days": (12 / 10),
        "120 days": 3,
    }
    report["pull_requests"] = {
        "30 days": 4,
        "60 days": 6,
        "90 days": 8,
        "120 days": 10,
        "150 days": 10,
        "1 year": 30,
    }
    return render_template(
        'archived_report.html',
        title='Team Report',
        data=report,
        raw_input={"raw_input": report["raw_input"]},
        report=report["report"],
    )
