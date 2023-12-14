#!/usr/bin/env python3

import ast
from flask import Flask, render_template, request, json
from flask import Blueprint
from DirectReport.browserview.app import login_required
from flask_login import login_required, current_user
from DirectReport.models.report_builder import ReportBuilder
from DirectReport.models.report_model import ReportModel
from DirectReport.models.entry_storage import EntryStorage
from DirectReport.models.list_builder import ListBuilder
from DirectReport.browserview.github import GithubClient
from DirectReport.browserview.github import GoogleAIClient

reportsbp = Blueprint('reportsbp', __name__)

@reportsbp.route("/report", methods=['GET', 'POST'])
@login_required
def report():
    prompt = ""
    prompt = request.get_json()["prompt"]
    client = GithubClient()
    user_repos = client.get_user_repos("chriswebb09")
    for repo in user_repos:
        print(repo)
    log_item = "Adrian Prantl (67):\n add mangling testcase\n Debug Info: Represent private discriminators in DWARF.\n Revert \"Debug Info: Represent private discriminators in DWARF.\n Debug Info: Represent private discriminators in DWARF.\n Un-XFAIL and update test.\n Move the logic for ignoring the debug locations for closure setup code into SILGen. NFC-ish.\n Debug Info: Associate a function call with the beginning of the expression.\n Debug Info / SILGen: fix the source location of variable assignments\n typo\n Fix the debug locations of inserted operations in AvailableValueAggregator.\n Don't emit shadow copies for anonymous variables.\n Remove dead API IRGenDebugInfo::setArtificialTrapLocation().\n Use compiler-generated location for func.-sig.-spec. thunks\n whitespace\n Fix the missing inlined-at field of function-level SILDebugScopes.\n Add debug info support for inlined and specialized generic variables.\n Revert Add debug info support for inlined and specialized generic variables.\n Add debug info support for inlined and specialized generic variables.\n Update mangling prefix in Mangling.rst\n Add initial support for debug info for coroutine allocas.\n Temporarily disable failing test case, rdar://problem/43340064\n Add build-script support for the Swift LLDB backwards-compatibility tests.\n Remove accidentally committed debugging code\n Deserialize Swift compatibility version in CompilerInvocation::loadFromSerializedAST()\n SILGen: Preserve function argument debug info for arguments needing alloc_stack\n Use as the filename for SILLocation-less functions to avoid misleading source locatio\nns in backtraces.\n Add a -verify-linetable LLVM option.\n Enable debug info for inlined generics by default. It works now.\n Fix nonasserts compilation\n\nAhmad Alhashemi (5):\n [Parser] Detect nonbreaking space U+00A0 and fixit\n Move non-breaking space handling to lexUnknown\n Add more non-breaking space test cases\n Minor style edits\n Add tests for non-breaking space detect and fix-it\n\nAkshay Shrimali (1):\n Update README.md\n\nAlan Zeino (1):\n Fix typo in code example in libSyntax README\n\nAlbin Sadowski (1):\n Fix syntax highlighting in CHANGELOG (#15107)\n\nAlejandro (3):\n Remove a warning, some doc fixes (#16863)\n [SR-8178] Fix BinaryFloatingPoint.random(in:) open range returning upperBound (#17794)\n [Docs] Fix minor code typo in SILPro..Man..md\n\nAlex Blewitt (5):\n [SR-7032] Fix compare for lhs and rhs\n [SR-7036] Use || instead of && for kind comparison\n [SR-7041] Remove duplicate conditional check\n Remove duplicate verb\n [SR-7043] Remove duplicate if statement"
    googleAi = GoogleAIClient()
    response_data = googleAi.get_data_from(prompt).replace("\'", "\"")
    response_data = response_data.replace("\n", " ")
    data_json = json.loads(response_data)
    data_json["broad_categories"] = {"debug_info": 16, "code_maintenance": 9, "documentation": 7, "test_related": 6, "nonbreaking_space_handling": 5, "readme_update": 1, "syntax_fix": 1}
    data_json["shortlog"] = client.parse_git_shortlog(log_item)
    ReportBuilder.new(data_json, prompt, current_user.id)
    return data_json, 201

@reportsbp.route("/teamreport", methods=['GET', 'POST'])
@login_required
def team_report():
    if request.method == "POST":
        json_data = request.get_json()
        report_model = ReportModel(json_data["id"], json_data['summary'], json_data['created_at'])
    return render_template('teamreport.html', title='Team Report', data=[])

@reportsbp.route('/entry/<uid>', methods=['GET', 'POST'])
@login_required
def detail(uid=None):
    """
    Retrieves and renders the details of a specific entry.

    :param uid: The ID of the entry to display.
    :return: Rendered HTML template for the entry details page.
    """
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    report = list(filter(lambda report: report["uuid"] == uid, reports))[0]
    json.loads(json.dumps(report))
    item = EntryStorage('SQLite_Python.db')
    if request.method == "POST":
        json_data = request.get_json()
        ListBuilder.update(
            json_data["id"], json_data['entry'], json_data['topic'], json_data['created_at'], json_data['week_id']
        )
    entry = item.get_entry(uid).to_dict()
    return render_template('detail.html', title='Detail', data=reportJSON)

@reportsbp.route("/getreport/<uid>", methods=['GET'])
@login_required
def get_report(uid=None):
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    report = list(filter(lambda report: report["uuid"] == uid, reports))[0]
    return report, 201

@reportsbp.route("/getlist", methods=['GET'])
@login_required
def get_list():
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    return reports, 201

@reportsbp.route("/list", methods=['GET', 'POST'])
@login_required
def list_entries():
    """
    Retrieves and renders the list of all entries.
    :return: Rendered HTML template for the list page.
    """
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    report_results = []
    for report in reports:
        report_element = {
            "report": report
        }
        report_results.append(report_element)
    return render_template('list.html', title='List', data=report_results)
