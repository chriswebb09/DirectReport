#!/usr/bin/env python3

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash
from DirectReport.browserview.auth import bp
from DirectReport.browserview.services.github import GithubClient
from DirectReport.datadependencies import appsecrets
from DirectReport.models.report.report_builder import ReportBuilder
from DirectReport.models.user_model import UserModel

user_model = UserModel()


@bp.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # code to validate and add user to database goes here
        email = request.form.get('email')
        username = request.form.get('username')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password_text = request.form.get('password')
        password = generate_password_hash(password_text)
        user_model.insert_user(email, username, firstname, lastname, email, password)
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html')


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = user_model.get_user_by_email(email)
        if user and user.check_password(password):
            login_user(user, remember=remember, force=True)
            if current_user.is_authenticated():
                return redirect(url_for('dashboard.dashboard_home'))
        else:
            print("password no match")
            flash("Please check your login details and try again.")
    return render_template(
        'auth/login.html', client_id=appsecrets.GITHUB_CLIENT_ID, client_secret=appsecrets.GITHUB_CLIENT_SECRET
    )


@bp.route("/account_data", methods=['GET'])
@login_required
def account_data():
    saved_reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    logitem = "Adrian Prantl (67):\n add mangling testcase\n Debug Info: Represent private discriminators in DWARF.\n Revert Debug Info: Represent private discriminators in DWARF.\"\n Debug Info: Represent private discriminators in DWARF.\n Un-XFAIL and update test.\n Move the logic for ignoring the debug locations for closure setup code into SILGen. NFC-ish.\n Debug Info: Associate a function call with the beginning of the expression.\n Debug Info / SILGen: fix the source location of variable assignments\n typo\n Fix the debug locations of inserted operations in AvailableValueAggregator.\n Don't emit shadow copies for anonymous variables.\n Remove dead API IRGenDebugInfo::setArtificialTrapLocation().\n Use compiler-generated location for func.-sig.-spec. thunks\n whitespace\n Fix the missing inlined-at field of function-level SILDebugScopes.\n Add debug info support for inlined and specialized generic variables.\n Revert Add debug info support for inlined and specialized generic variables.\"\n Add debug info support for inlined and specialized generic variables.\n Update mangling prefix in Mangling.rst\n Add initial support for debug info for coroutine allocas.\n Temporarily disable failing test case, rdar://problem/43340064\n Add build-script support for the Swift LLDB backwards-compatibility tests.\n Remove accidentally committed debugging code\n Deserialize Swift compatibility version in CompilerInvocation::loadFromSerializedAST()\n SILGen: Preserve function argument debug info for arguments needing alloc_stack\n Use as the filename for SILLocation-less functions to avoid misleading source locatio\nns in backtraces.\n Add a -verify-linetable LLVM option.\n Enable debug info for inlined generics by default. It works now.\n Fix nonasserts compilation\n\nAhmad Alhashemi (5):\n [Parser] Detect nonbreaking space U+00A0 and fixit\n Move non-breaking space handling to lexUnknown\n Add more non-breaking space test cases\n Minor style edits\n Add tests for non-breaking space detect and fix-it\n\nAkshay Shrimali (1):\n Update README.md\n\nAlan Zeino (1):\n Fix typo in code example in libSyntax README\n\nAlbin Sadowski (1):\n Fix syntax highlighting in CHANGELOG (#15107)\n\nAlejandro (3):\n Remove a warning, some doc fixes (#16863)\n [SR-8178] Fix BinaryFloatingPoint.random(in:) open range returning upperBound (#17794)\n [Docs] Fix minor code typo in SILPro..Man..md\n\nAlex Blewitt (5):\n [SR-7032] Fix compare for lhs and rhs\n [SR-7036] Use || instead of && for kind comparison\n [SR-7041] Remove duplicate conditional check\n Remove duplicate verb\n [SR-7043] Remove duplicate if statement"
    client = GithubClient()
    shortlog = client.parse_git_shortlog(logitem)
    report_results = []
    for report in saved_reports:
        report_element = {"report": report}
        report_results.append(report_element)
    user_account = {
        "name": current_user.firstname + " " + current_user.lastname,
        "firstname": current_user.firstname,
        "lastname": current_user.lastname,
        "userid": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "github_username": current_user.github_username,
    }
    user_element = {"user": user_account, "reports": report_results, "shortlog": shortlog}
    return user_element, 201
