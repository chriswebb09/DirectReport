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
        name = request.form.get('name')
        username = request.form.get('username')
        passwordtext = request.form.get('password')
        password = generate_password_hash(passwordtext)
        user_model.insert_user(username, name, email, password)
         # insert_user(name, email, password))
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
    users = user_model.get_all_users()
    print("user loader")
    print(user)
    print(users)
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
    entries_list  = {
        "name": current_user.username,
        "userid": current_user.id
    }
    return entries_list, 201


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

# @app.route("/team/<uid>", methods=['GET', 'POST'])
# def team_report():
#     if request.method == "POST":
#         print("POST")
#     return render_template('team_member.html', title='Team Member', data=[])

@app.route("/report", methods=['GET', 'POST'])
@login_required
def report():
    prompt = ""
    prompt = request.get_json()["prompt"]
    elements = TEST_DATA_ELEMENTS
    client = GithubClient()
    # elements["shortlog"] = client.parse_git_shortlog(logitem)
    # ReportBuilder.new(elements["report"], prompt, current_user.id)
    print(ReportBuilder.get_reports_for_user_id(current_user.id))
    # if request.method == "POST":
    #
    #
    # # builder = ReportBuilder()
    # ReportBuilder.new(elements["report"])
    # list = ReportBuilder.list_all()
    # print(list)
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
