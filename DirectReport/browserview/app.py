#!/usr/bin/env python3

# Flask

from DirectReport.models.list_builder import ListBuilder
from DirectReport.models.weekly_builder import WeeklyBuilder
from DirectReport.database.entry_storage import EntryStorage
from flask import Flask, render_template, request, redirect

# AI Models

import openai
import secrets

openai.api_key = secrets.SECRET_KEY

app = Flask(__name__, template_folder="templates")

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


@app.route("/teamreport", methods=['GET', 'POST'])
def teamreport():
    report = get_team_summarys_from_git_shortlog("Adrian Prantl (67):\n add mangling testcase\n Debug Info: Represent private discriminators in DWARF.\n Revert \"Debug Info: Represent private discriminators in DWARF.\"\n Debug Info: Represent private discriminators in DWARF.\n Un-XFAIL and update test.\n Move the logic for ignoring the debug locations for closure setup code into SILGen. NFC-ish.\n Debug Info: Associate a function call with the beginning of the expression.\n Debug Info / SILGen: fix the source location of variable assignments\n typo\n Fix the debug locations of inserted operations in AvailableValueAggregator.\n Don't emit shadow copies for anonymous variables.\n Remove dead API IRGenDebugInfo::setArtificialTrapLocation().\n Use compiler-generated location for func.-sig.-spec. thunks\n whitespace\n Fix the missing inlined-at field of function-level SILDebugScopes.\n Add debug info support for inlined and specialized generic variables.\n Revert \"Add debug info support for inlined and specialized generic variables.\"\n Add debug info support for inlined and specialized generic variables.\n Update mangling prefix in Mangling.rst\n Add initial support for debug info for coroutine allocas.\n Temporarily disable failing test case, rdar://problem/43340064\n Add build-script support for the Swift LLDB backwards-compatibility tests.\n Remove accidentally committed debugging code\n Deserialize Swift compatibility version in CompilerInvocation::loadFromSerializedAST()\n SILGen: Preserve function argument debug info for arguments needing alloc_stack\n Use as the filename for SILLocation-less functions to avoid misleading source locatio\nns in backtraces.\n Add a -verify-linetable LLVM option.\n Enable debug info for inlined generics by default. It works now.\n Fix nonasserts compilation\n\nAhmad Alhashemi (5):\n [Parser] Detect nonbreaking space U+00A0 and fixit\n Move non-breaking space handling to lexUnknown\n Add more non-breaking space test cases\n Minor style edits\n Add tests for non-breaking space detect and fix-it\n\nAkshay Shrimali (1):\n Update README.md\n\nAlan Zeino (1):\n Fix typo in code example in libSyntax README\n\nAlbin \"albinek\" Sadowski (1):\n Fix syntax highlighting in CHANGELOG (#15107)\n\nAlejandro (3):\n Remove a warning, some doc fixes (#16863)\n [SR-8178] Fix BinaryFloatingPoint.random(in:) open range returning upperBound (#17794)\n [Docs] Fix minor code typo in SILPro..Man..md\n\nAlex Blewitt (5):\n [SR-7032] Fix compare for lhs and rhs\n [SR-7036] Use || instead of && for kind comparison\n [SR-7041] Remove duplicate conditional check\n Remove duplicate verb\n [SR-7043] Remove duplicate if statement")
    return render_template('teamreport.html', title='Team Report', data={report})

def new():
    """
    Retrieves and renders the list of all entries.

    :return: Rendered HTML template for the list page.
    """
    return render_template('list.html', title='New Entry', data=[])


@app.route("/list", methods=['GET', 'POST'])
def list_entries():
    """
    Retrieves and renders the list of all entries.

    :return: Rendered HTML template for the list page.
    """
    if request.method == "POST":
        json_data = request.get_json()
        ListBuilder.new(json_data["entry"], json_data["topic"])
    week_id = WeeklyBuilder.get_weekly_id()
    week = WeeklyBuilder.list_week(week_id)
    print(week)
    return render_template('list.html', title='List', data=week)


@app.route('/entry/<uid>', methods=['GET', 'POST'])
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


@app.route('/delete/<id>', methods=['GET'])
def delete(uid=None):
    """
    Deletes a specific entry and redirects to the list page.

    :param uid: The ID of the entry to delete.
    :return: Redirects to the '/list' route.
    """
    item = EntryStorage('SQLite_Python.db')
    item.delete_entry(uid)
    return redirect("/list", code=302)


def get_team_summarys_from_git_shortlog(data):
    prompt =  "can you provide a short summary of what the team as a whole accomplished this week as well as an individual breakdown based on the following list of team members and work using the following" + "Format: \n" + "{ \n" + "'team'" + ": [{" + "\n 'name'" + ": '', " + "\n 'accomplishments'" + ": '' " + " ," + "\n 'commits'" + ": '' \n" + "}]," + "\n'report'" + ": {" + "\n 'summary'" + ": " + "\n  'highlights'" + ": [{" + "\n   'title'" + ": '' ," + "\n   'description'" + ": '' "+ "\n }], \n" + " 'conclusion'" + ": ''" + "\n}" + "\n}" + "\n" + "Data:" + data
    message=[{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.2,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    app.run()
