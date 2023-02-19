#!/usr/bin/env python

from flask import Flask

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    """Homepage"""
    return render_template('index.html', title='Home')

def run_app():
    app.run()

print(__name__)

if __name__ == '__main__':
    run_app()
