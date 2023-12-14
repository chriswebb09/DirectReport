#!/usr/bin/env python3

import ast
from flask import Flask, render_template, request, json
from flask import Blueprint
from DirectReport.browserview.app import login_required
from flask_login import login_required, current_user
from .modelclient import RAW_REPORT_DATA
from .modelclient import RAW_REPORT_DATA_2
from DirectReport.models.report_builder import ReportBuilder
from DirectReport.browserview.github import GithubClient
from DirectReport.browserview.github import GoogleAIClient

reportsbp = Blueprint('reportsbp', __name__)

@reportsbp.route("/report", methods=['GET', 'POST'])
@login_required
def report():
    prompt = ""
    prompt = request.get_json()["prompt"]
    elements = RAW_REPORT_DATA_2
    client = GithubClient()
    user_repos = client.get_user_repos("chriswebb09")
    for repo in user_repos:
        print(repo)
        # print(repo["name"])
        # print(repo["full_name"])
        # print(repo["html_url"])
        # print(repo["language"])
        # print(repo["description"])
        # print(repo["stargazers_count"])
        # print(repo["watchers_count"])
        # print("\n")
    logitem = "Adrian Prantl (67):\n add mangling testcase\n Debug Info: Represent private discriminators in DWARF.\n Revert \"Debug Info: Represent private discriminators in DWARF.\n Debug Info: Represent private discriminators in DWARF.\n Un-XFAIL and update test.\n Move the logic for ignoring the debug locations for closure setup code into SILGen. NFC-ish.\n Debug Info: Associate a function call with the beginning of the expression.\n Debug Info / SILGen: fix the source location of variable assignments\n typo\n Fix the debug locations of inserted operations in AvailableValueAggregator.\n Don't emit shadow copies for anonymous variables.\n Remove dead API IRGenDebugInfo::setArtificialTrapLocation().\n Use compiler-generated location for func.-sig.-spec. thunks\n whitespace\n Fix the missing inlined-at field of function-level SILDebugScopes.\n Add debug info support for inlined and specialized generic variables.\n Revert Add debug info support for inlined and specialized generic variables.\n Add debug info support for inlined and specialized generic variables.\n Update mangling prefix in Mangling.rst\n Add initial support for debug info for coroutine allocas.\n Temporarily disable failing test case, rdar://problem/43340064\n Add build-script support for the Swift LLDB backwards-compatibility tests.\n Remove accidentally committed debugging code\n Deserialize Swift compatibility version in CompilerInvocation::loadFromSerializedAST()\n SILGen: Preserve function argument debug info for arguments needing alloc_stack\n Use as the filename for SILLocation-less functions to avoid misleading source locatio\nns in backtraces.\n Add a -verify-linetable LLVM option.\n Enable debug info for inlined generics by default. It works now.\n Fix nonasserts compilation\n\nAhmad Alhashemi (5):\n [Parser] Detect nonbreaking space U+00A0 and fixit\n Move non-breaking space handling to lexUnknown\n Add more non-breaking space test cases\n Minor style edits\n Add tests for non-breaking space detect and fix-it\n\nAkshay Shrimali (1):\n Update README.md\n\nAlan Zeino (1):\n Fix typo in code example in libSyntax README\n\nAlbin Sadowski (1):\n Fix syntax highlighting in CHANGELOG (#15107)\n\nAlejandro (3):\n Remove a warning, some doc fixes (#16863)\n [SR-8178] Fix BinaryFloatingPoint.random(in:) open range returning upperBound (#17794)\n [Docs] Fix minor code typo in SILPro..Man..md\n\nAlex Blewitt (5):\n [SR-7032] Fix compare for lhs and rhs\n [SR-7036] Use || instead of && for kind comparison\n [SR-7041] Remove duplicate conditional check\n Remove duplicate verb\n [SR-7043] Remove duplicate if statement"
    googleAi = GoogleAIClient()
    response_data = googleAi.get_data_from(prompt).replace("\'", "\"")
    response_data = response_data.replace("\n", " ")
    data_json = json.loads(response_data)
    data_json["broad_categories"] = {"debug_info": 16, "code_maintenance": 9, "documentation": 7, "test_related": 6, "nonbreaking_space_handling": 5, "readme_update": 1, "syntax_fix": 1}
    data_json["shortlog"] = client.parse_git_shortlog(logitem)
    ReportBuilder.new(data_json, prompt, current_user.id)
    return data_json, 201

@reportsbp.route("/teamreport", methods=['GET', 'POST'])
@login_required
def team_report():
    if request.method == "POST":
        print("POST")
        # json_data = request.get_json()
        # report_model = ReportModel(json_data["id"], json_data['summary'], json_data['created_at'])
        # print("POST")
    return render_template('teamreport.html', title='Team Report', data=[])

@reportsbp.route('/entry/<uid>', methods=['GET', 'POST'])
@login_required
def detail(uid=None):
    """
    Retrieves and renders the details of a specific entry.

    :param uid: The ID of the entry to display.
    :return: Rendered HTML template for the entry details page.
    """
    # print(uid)
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    # report = list(filter(lambda report: report["uuid"] == uid, reports))[0]
    # print(report)
    reportJSON = {'report': {
        'broad_categories': {'code_maintenance': 9, 'debug_info': 16, 'documentation': 7, 'nonbreaking_space_handling': 5, 'readme_update': 1, 'syntax_fix': 1, 'test_related': 6},
        'report': {
            'areas_of_focus': ['DebugInfo and SILGen Enhancements', 'Parser Improvements', 'Various Fixes'],
            'conclusion': 'The team demonstrated good progress this week, with a focus on enhancing DebugInfo and SILGen, improving the Parser, and implementing various fixes. The team should continue to focus on these areas in the coming week.',
            'highlights': [
                {'description': 'Adrian Prantl made significant contributions to the DebugInfo and SILGen, including adding support for debuginfo for coroutine allocas, inlined and specialized generic variables.', 'title': 'DebugInfo and SILGen Enhancements'},
                {'description': 'Ahmad Alhashemi worked on the Parser, detecting non-breaking space U+00A0 and providing a fix.', 'title': 'Parser Improvements'},
                {'description': 'The team worked on several fixes including compare for lhs and rhs, using || instead of && for kind comparison, removing duplicate conditional check and duplicate if statement.', 'title': 'Various Fixes'}
            ],
            'summary': 'The team made significant progress this week with a total of 83 commits. The main focus was on DebugInfo and SILGen enhancements, Parser improvements, and various fixes.',
            'total_commits': '83'
        },
        'shortlog': {'Adrian Prantl': 67, 'Ahmad Alhashemi': 5, 'Akshay Shrimali': 1, 'Alan Zeino': 1, 'Albin Sadowski': 1, 'Alejandro': 3, 'Alex Blewitt': 5},
        'team': [
            {'accomplishments': 'Adrian made significant contributions to the DebugInfo and SILGen, including adding support for debug info for coroutine allocas, inlined and specialized generic variables. He also worked on the mangling testcase, fixed source locations of variable assignments and function calls, and added build-script support for Swift LLDB backwards-compatibility tests.', 'commits': '67', 'name': 'Adrian Prantl'},
            {'accomplishments': 'Alan fixed a typo in the code example in libSyntax README.', 'commits': '1', 'name': 'Alan Zeino'},
            {'accomplishments': 'Alejandro removed a warning, made some documentation fixes, fixed Binary Floating Point. random(in:) open range returning upperBound, and fixed a minor code typo in SILPro.', 'commits': '3', 'name': 'Alejandro'},
            {'accomplishments': 'Akshay updated the README.md file.', 'commits': '1', 'name': 'Akshay Shrimali'},
            {'accomplishments': 'Ahmad worked on the Parser, detecting non-breaking space U+00A0 and providing a fix. He also made minor style edits and added more non-breaking space testcases.', 'commits': '5', 'name': 'Ahmad Alhashemi'},
            {'accomplishments': 'Albin fixed syntax highlighting in CHANGELOG.', 'commits': '1', 'name': 'Albin Sadowski'},
            {'accomplishments': 'Alex worked on several fixes including compare for lhs and rhs, using || instead of && for kind comparison, removing duplicate conditional check and duplicate if statement.', 'commits': '5', 'name': 'Alex Blewitt'}
        ]
    },
        'created_at': '1702314769.558132'}

    # json.loads(json.dumps(report))
    # report = {}
    # item = EntryStorage('SQLite_Python.db')
    # if request.method == "POST":
    #     json_data = request.get_json()
    #     ListBuilder.update(
    #         json_data["id"], json_data['entry'], json_data['topic'], json_data['created_at'], json_data['week_id']
    #     )
    # entry = item.get_entry(uid).to_dict()
    return render_template('detail.html', title='Detail', data=reportJSON)

@reportsbp.route("/getreport/<uid>", methods=['GET'])
@login_required
def get_report(uid=None):
    print(uid)
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    # report = list(filter(lambda report: report["uuid"] == uid, reports))[0]
    # hugClient = HuggingFaceClient()
    # result = hugClient.query({
    #     "inputs": "Can you please let us know more details about your ",
    # })
    return RAW_REPORT_DATA_2, 201

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
    print(reports)
    report_results = []
    for report in reports:
        report_element = {
            "report": report
        }
        report_results.append(report_element)
    return render_template('list.html', title='List', data=report_results)
