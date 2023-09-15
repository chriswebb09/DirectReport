#!/usr/bin/env python3

# Flask

from flask import Flask, render_template, request, redirect, jsonify, json

# OpenAI 

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
def team_report():
    if request.method == "POST":
        print("POST")
    return render_template('teamreport.html', title='Team Report', data=[])


@app.route("/report", methods=['GET', 'POST'])
def report():
    prompt = ""
    if request.method == "POST":
        print("POST")
        prompt = request.get_json()["prompt"]
    report = get_team_summarys_from_git_shortlog(prompt);
    elements = report.choices[0].message.content
    elements = elements.replace("'", '"')
    elements = elements.replace('"albinek"', '')
    json_object = json.loads(elements)
    return json_object, 201


def new():
    """
    Retrieves and renders the list of all entries.

    :return: Rendered HTML template for the list page.
    """
    return render_template('list.html', title='New Entry', data=[])

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
    return response


if __name__ == "__main__":
    app.run()
