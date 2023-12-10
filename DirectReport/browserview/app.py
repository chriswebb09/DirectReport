#!/usr/bin/env python3

# Flask
from flask import Flask, render_template, request, redirect, json, url_for
from werkzeug.security import generate_password_hash
from DirectReport.models.user_model import UserModel
from DirectReport.models.list_builder import ListBuilder
from DirectReport.models.report_model import ReportModel
from DirectReport.models.report_builder import ReportBuilder
from DirectReport.models.report import Report
from DirectReport.browserview.prompt_logic import generate_email
from DirectReport.browserview.github import GithubClient
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from DirectReport.datadependencies import appsecrets
from .auth.auth import auth
from .modelclient import TEST_DATA_ELEMENTS

login_manager = LoginManager()
app = Flask(__name__, template_folder="templates")
app.register_blueprint(auth)
app.secret_key = appsecrets.SECRET_KEY
login_manager.init_app(app)
login_manager.login_view = "login"
user_model = UserModel()

@app.route("/")
def home():
    """
    Renders the homepage of the web application.
    :return: Rendered HTML template for the homepage.
    """
    return render_template('index.html', title='Home')

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors (page not found).

    :param e: The error object.
    :return: Rendered HTML template for the 404 error page.
    """
    return render_template('404.html', error=e), 404

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # code to validate and add user to database goes here
        email = request.form.get('email')
        username = request.form.get('username')
        firstname= request.form.get('firstname')
        lastname = request.form.get('lastname')
        passwordtext = request.form.get('password')
        password = generate_password_hash(passwordtext)
        user_model = UserModel()
        user_model.insert_user(email, username, firstname, lastname, email, password)
         # insert_user(username, firstname, lastname, email, password))
        return redirect(url_for('login'))
    return render_template('auth/signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # remember = True if request.form.get('remember') else False
        user = user_loader(email)
        login_user(user, remember=True, force=True)
        if current_user.is_authenticated():
            return redirect(url_for('account'))
    return render_template('auth/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('team_report'))

@login_manager.user_loader
def user_loader(email):
    user = user_model.get_user_by_email(email)
    return user

@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    user = user_model.get_user_by_email(email)
    return user

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account.html', title='Account', name=current_user.username, userid=current_user.id)

@app.route("/account_data", methods=['GET'])
@login_required
def account_data():
    user_account  = {
        "name": current_user.firstname + " " + current_user.lastname,
        "first_name": current_user.firstname,
        "last_name": current_user.lastname,
        "userid": current_user.id,
        "email": current_user.email,
        "username": current_user.username,
        "firstname": current_user.firstname,
        "lastname": current_user.lastname
    }
    return user_account, 201


@app.route("/list", methods=['GET', 'POST'])
@login_required
def list_entries():
    """
    Retrieves and renders the list of all entries.
    :return: Rendered HTML template for the list page.
    """
    entries_list = ListBuilder.list_all()
    return render_template('list.html', title='List', data=entries_list)

@app.route("/getlist", methods=['GET'])
@login_required
def get_list():
    entries_list = ListBuilder.list_all()
    return entries_list, 201

@app.route('/entry/<uid>', methods=['GET', 'POST'])
@login_required
def detail(uid=None):
    """
    Retrieves and renders the details of a specific entry.

    :param uid: The ID of the entry to display.
    :return: Rendered HTML template for the entry details page.
    """
    item = EntryStorage('SQLite_Python.db')
    if request.method == "POST":
        json_data = request.get_json()
        ListBuilder.update(
            json_data["id"], json_data['entry'], json_data['topic'], json_data['created_at'], json_data['week_id']
        )
    entry = item.get_entry(uid).to_dict()
    return render_template('detail.html', title='Detail', data=entry)

@app.route("/new", methods=['GET', 'POST'])
@login_required
def new():
    """
    Retrieves and renders the list of all entries.
    :return: Rendered HTML template for the list page.
    """
    return render_template('list.html', title='New Entry', data=[])

@login_manager.unauthorized_handler
def unauthorized_handler():
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return redirect(url_for('login'))
    else:
        if current_user.is_authenticated:
            return redirect(url_for('account'))
        else:
            return redirect(url_for('login'))

@app.route("/teamreport", methods=['GET', 'POST'])
@login_required
def team_report():
    if request.method == "POST":
        print("POST")
        # json_data = request.get_json()
        # report_model = ReportModel(json_data["id"], json_data['summary'], json_data['created_at'])
        # print("POST")
    return render_template('teamreport.html', title='Team Report', data=[])

@app.route("/team", methods=['GET'])
def team():
    return render_template('team.html', title='Team', data=[])

@app.route("/report", methods=['GET', 'POST'])
@login_required
def report():
    prompt = ""
    prompt = request.get_json()["prompt"]
    elements = TEST_DATA_ELEMENTS
    client = GithubClient()
    logitem = "Adrian Prantl (67):\n add mangling testcase\n Debug Info: Represent private discriminators in DWARF.\n Revert \"Debug Info: Represent private discriminators in DWARF.\"\n Debug Info: Represent private discriminators in DWARF.\n Un-XFAIL and update test.\n Move the logic for ignoring the debug locations for closure setup code into SILGen. NFC-ish.\n Debug Info: Associate a function call with the beginning of the expression.\n Debug Info / SILGen: fix the source location of variable assignments\n typo\n Fix the debug locations of inserted operations in AvailableValueAggregator.\n Don't emit shadow copies for anonymous variables.\n Remove dead API IRGenDebugInfo::setArtificialTrapLocation().\n Use compiler-generated location for func.-sig.-spec. thunks\n whitespace\n Fix the missing inlined-at field of function-level SILDebugScopes.\n Add debug info support for inlined and specialized generic variables.\n Revert \"Add debug info support for inlined and specialized generic variables.\"\n Add debug info support for inlined and specialized generic variables.\n Update mangling prefix in Mangling.rst\n Add initial support for debug info for coroutine allocas.\n Temporarily disable failing test case, rdar://problem/43340064\n Add build-script support for the Swift LLDB backwards-compatibility tests.\n Remove accidentally committed debugging code\n Deserialize Swift compatibility version in CompilerInvocation::loadFromSerializedAST()\n SILGen: Preserve function argument debug info for arguments needing alloc_stack\n Use as the filename for SILLocation-less functions to avoid misleading source locatio\nns in backtraces.\n Add a -verify-linetable LLVM option.\n Enable debug info for inlined generics by default. It works now.\n Fix nonasserts compilation\n\nAhmad Alhashemi (5):\n [Parser] Detect nonbreaking space U+00A0 and fixit\n Move non-breaking space handling to lexUnknown\n Add more non-breaking space test cases\n Minor style edits\n Add tests for non-breaking space detect and fix-it\n\nAkshay Shrimali (1):\n Update README.md\n\nAlan Zeino (1):\n Fix typo in code example in libSyntax README\n\nAlbin \"albinek\" Sadowski (1):\n Fix syntax highlighting in CHANGELOG (#15107)\n\nAlejandro (3):\n Remove a warning, some doc fixes (#16863)\n [SR-8178] Fix BinaryFloatingPoint.random(in:) open range returning upperBound (#17794)\n [Docs] Fix minor code typo in SILPro..Man..md\n\nAlex Blewitt (5):\n [SR-7032] Fix compare for lhs and rhs\n [SR-7036] Use || instead of && for kind comparison\n [SR-7041] Remove duplicate conditional check\n Remove duplicate verb\n [SR-7043] Remove duplicate if statement"
    elements["shortlog"] = client.parse_git_shortlog(logitem)
    print(ReportBuilder.get_reports_for_user_id(current_user.id))
    return elements, 201

@app.route("/generate_email", methods=['POST'])
def generate_email():
    prompt = ""
    if request.method == "POST":
        prompt = json.dumps(request.get_json()["prompt"])
    report = generate_email(prompt)
    elements = {"email": report.choices[0].message.content}
    return elements, 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)
