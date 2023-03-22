#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    """Homepage"""
    return render_template('index.html', title='Home')


if __name__ == "__main__":
    app.run()
