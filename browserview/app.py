#!/usr/bin/env python

from flask import Flask

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    """Homepage"""
    return render_template('index.html', title='Home')
