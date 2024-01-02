#!/usr/bin/env python3

import requests
from flask import render_template, session, request, redirect, json, jsonify
from flask_login import login_user, login_required, logout_user, current_user

from DirectReport.browserview.dashboard import bp
from DirectReport.models.report.report_builder import ReportBuilder
from DirectReport.browserview.services.github import GithubClient
from DirectReport.browserview.services.github import GoogleAIClient
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
    print(results)
    return render_template('list.html', title='List', data=results)


@bp.route("/reports/new", methods=['GET', 'POST'])
@login_required
def dashboard_reports_new():
    if request.method == "POST":
        json_data = request.get_json()
        report_model = ReportModel(json_data["id"], json_data['summary'], json_data['created_at'])
    return render_template('team/teamreport.html', title='Team Report', data=[])


@bp.route("/reports/update", methods=['GET', 'POST'])
@login_required
def dashboard_reports_update():
    prompt = ""
    prompt = request.get_json()["prompt"]
    client = GithubClient()
    user_repos = client.get_user_repos(current_user.github_username)
    repodata = []
    for repo in user_repos:
        repodata.append(repo["name"])
    log_item = "Adrian Prantl (67):\n add mangling testcase\n Debug Info: Represent private discriminators in DWARF.\n Revert \"Debug Info: Represent private discriminators in DWARF.\n Debug Info: Represent private discriminators in DWARF.\n Un-XFAIL and update test.\n Move the logic for ignoring the debug locations for closure setup code into SILGen. NFC-ish.\n Debug Info: Associate a function call with the beginning of the expression.\n Debug Info / SILGen: fix the source location of variable assignments\n typo\n Fix the debug locations of inserted operations in AvailableValueAggregator.\n Don't emit shadow copies for anonymous variables.\n Remove dead API IRGenDebugInfo::setArtificialTrapLocation().\n Use compiler-generated location for func.-sig.-spec. thunks\n whitespace\n Fix the missing inlined-at field of function-level SILDebugScopes.\n Add debug info support for inlined and specialized generic variables.\n Revert Add debug info support for inlined and specialized generic variables.\n Add debug info support for inlined and specialized generic variables.\n Update mangling prefix in Mangling.rst\n Add initial support for debug info for coroutine allocas.\n Temporarily disable failing test case, rdar://problem/43340064\n Add build-script support for the Swift LLDB backwards-compatibility tests.\n Remove accidentally committed debugging code\n Deserialize Swift compatibility version in CompilerInvocation::loadFromSerializedAST()\n SILGen: Preserve function argument debug info for arguments needing alloc_stack\n Use as the filename for SILLocation-less functions to avoid misleading source locatio\nns in backtraces.\n Add a -verify-linetable LLVM option.\n Enable debug info for inlined generics by default. It works now.\n Fix nonasserts compilation\n\nAhmad Alhashemi (5):\n [Parser] Detect nonbreaking space U+00A0 and fixit\n Move non-breaking space handling to lexUnknown\n Add more non-breaking space test cases\n Minor style edits\n Add tests for non-breaking space detect and fix-it\n\nAkshay Shrimali (1):\n Update README.md\n\nAlan Zeino (1):\n Fix typo in code example in libSyntax README\n\nAlbin Sadowski (1):\n Fix syntax highlighting in CHANGELOG (#15107)\n\nAlejandro (3):\n Remove a warning, some doc fixes (#16863)\n [SR-8178] Fix BinaryFloatingPoint.random(in:) open range returning upperBound (#17794)\n [Docs] Fix minor code typo in SILPro..Man..md\n\nAlex Blewitt (5):\n [SR-7032] Fix compare for lhs and rhs\n [SR-7036] Use || instead of && for kind comparison\n [SR-7041] Remove duplicate conditional check\n Remove duplicate verb\n [SR-7043] Remove duplicate if statement"
    googleAi = GoogleAIClient()
    response_data = googleAi.get_data_from(prompt)
    response_data["broad_categories"] = {
        "debug_info": 16,
        "code_maintenance": 9,
        "documentation": 7,
        "test_related": 6,
        "nonbreaking_space_handling": 5,
        "readme_update": 1,
        "syntax_fix": 1,
    }
    response_data["shortlog"] = client.parse_git_shortlog(log_item)
    response_data["repos"] = repodata
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