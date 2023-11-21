#!/usr/bin/env python3
import flask

# Flask
from flask import Flask, render_template, request, redirect, jsonify, json, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from DirectReport.models.user_model import User, UserModel
from .prompt_logic import get_team_summarys_from_git_shortlog, generate_email
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

import appsecrets

login_manager = LoginManager()
app = Flask(__name__, template_folder="templates")
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

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    passwordtext = request.form.get('password')
    password = generate_password_hash(passwordtext)
    user_model.insert_user(name, email, password)
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    # remember = True if request.form.get('remember') else False
    user = user_loader(email)
    if request.method == 'POST':
        login_user(user, remember=True, force=True)
        if current_user.is_authenticated():
            return redirect(url_for('account'))
    return render_template('login.html')

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
    print(current_user.is_authenticated())
    return render_template('account.html', title='Account', name=current_user.username, userid=current_user.id)

@login_manager.unauthorized_handler
def unauthorized_handler():
    print("unauthorized_handler")
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return redirect(url_for('login'))
    else:
        if current_user.is_authenticated:
            return redirect(url_for('account'))
        else:
            return redirect(url_for('login'))

@app.route("/teamreport", methods=['GET', 'POST'])
def team_report():
    if request.method == "POST":
        print("POST")
    return render_template('teamreport.html', title='Team Report', data=[])

@app.route("/report", methods=['GET', 'POST'])
def report():
    prompt = ""
    if request.method == "POST":
        prompt = request.get_json()["prompt"]
    elements = {
        "team": [
            {
                "name": "AdrianPrantl",
                "accomplishments": "AdrianmadesignificantcontributionstotheDebugInfoandSILGen,includingaddingsupportfordebuginfoforcoroutineallocas,inlinedandspecializedgenericvariables.Healsoworkedonthemanglingtestcase,fixedsourcelocationsofvariableassignmentsandfunctioncalls,andaddedbuild-scriptsupportforSwiftLLDBbackwards-compatibilitytests.",
                "commits": "67"
            },
            {
                "name": "AhmadAlhashemi",
                "accomplishments": "AhmadworkedontheParser,detectingnonbreakingspaceU+00A0andprovidingafix.Healsomademinorstyleeditsandaddedmorenon-breakingspacetestcases.",
                "commits": "5"
            },
            {
                "name": "AkshayShrimali",
                "accomplishments": "AkshayupdatedtheREADME.mdfile.",
                "commits": "1"
            },
            {
                "name": "AlanZeino",
                "accomplishments": "AlanfixedatypointhecodeexampleinlibSyntaxREADME.",
                "commits": "1"
            },
            {
                "name": "Albin\"albinek\"Sadowski",
                "accomplishments": "AlbinfixedsyntaxhighlightinginCHANGELOG.",
                "commits": "1"
            },
            {
                "name": "Alejandro",
                "accomplishments": "Alejandroremovedawarning,madesomedocumentationfixes,fixedBinaryFloatingPoint.random(in:)openrangereturningupperBound,andfixedaminorcodetypoinSILPro..Man..md.",
                "commits": "3"
            },
            {
                "name": "AlexBlewitt",
                "accomplishments": "Alexworkedonseveralfixesincludingcompareforlhsandrhs,using||insteadof&&forkindcomparison,removingduplicateconditionalcheckandduplicateifstatement.",
                "commits": "5"
            }
        ],
        "report": {
            "summary": "Theteammadesignificantprogressthisweekwithatotalof83commits.ThemainfocuswasonDebugInfoandSILGenenhancements,Parserimprovements,andvariousfixes.",
            "total_commits": "83",
            "areas_of_focus": ["DebugInfoandSILGenEnhancements", "ParserImprovements", "VariousFixes"],
            "highlights": [
                {
                    "title": "DebugInfoandSILGenEnhancements",
                    "description": "AdrianPrantlmadesignificantcontributionstotheDebugInfoandSILGen,includingaddingsupportfordebuginfoforcoroutineallocas,inlinedandspecializedgenericvariables."
                },
                {
                    "title": "ParserImprovements",
                    "description": "AhmadAlhashemiworkedontheParser,detectingnonbreakingspaceU+00A0andprovidingafix."
                },
                {
                    "title": "VariousFixes",
                    "description": "Theteamworkedonseveralfixesincludingcompareforlhsandrhs,using||insteadof&&forkindcomparison,removingduplicateconditionalcheckandduplicateifstatement."
                }
            ],
            "conclusion": "Theteamdemonstratedgoodprogressthisweek,withafocusonenhancingDebugInfoandSILGen,improvingtheParser,andimplementingvariousfixes.Theteamshouldcontinuetofocusontheseareasinthecomingweek."
        }
    }
    # elements = {}
    # if prompt is not "":
    #     report = get_team_summarys_from_git_shortlog(prompt)
    #     elements = report.choices[0].message.content
    #     print(elements)
    #     elements = elements.replace("'", '"')
    #     elements = elements.replace('"albinek"', '')
    #     json_object = json.loads(elements)
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
    app.run()
