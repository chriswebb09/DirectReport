#!/usr/bin/env python3

# Flask

from flask import Flask, render_template, request, redirect, jsonify, json

# OpenAI 

import openai
import secrets
import prompts

openai.api_key = secrets.SECRET_KEY

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    """
    Renders the homepage of the web application.
    :return: Rendered HTML template for the homepage.
    """
    return render_template('index.html', title='Home')

@app.route("/account", methods=['GET', 'POST'])
def account():
    return render_template('account.html', title='Account')

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
        prompt = request.get_json()["prompt"]
    report = get_team_summarys_from_git_shortlog(prompt)
    elements = report.choices[0].message.content
    elements = elements.replace("'", '"')
    elements = elements.replace('"albinek"', '')
    json_object = json.loads(elements)
    return json_object, 201

@app.route("/generate_email", methods=['POST'])
def generate_email():
    prompt = ""
    if request.method == "POST":
        prompt = json.dumps(request.get_json()["prompt"])
    print(prompt)
    report = generate_email(prompt)
    elements = {"email": report.choices[0].message.content}
    return elements, 201

def new():
    """
    Retrieves and renders the list of all entries.

    :return: Rendered HTML template for the list page.
    """
    return render_template('list.html', title='New Entry', data=[])

def get_team_summarys_from_git_shortlog(data):
    prompt =  prompts.GENERATE_SUMMARY_PROMPT_PREIX + data
    message=[{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.1,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    return response

def generate_email(data):
    prompt =  prompts.GENERATE_EMAIL_PROMPT_PREFIX + data
    message=[{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages = message,
        temperature=0.1,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    print(response)
    return response


if __name__ == "__main__":
    app.run()
