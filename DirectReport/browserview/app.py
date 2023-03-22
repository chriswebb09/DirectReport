#!/usr/bin/env python3

from flask import Flask, render_template

from pathlib import Path

# file = Path(__file__).resolve()
# package_root_directory = file.parents[1]
# sys.path.append(str(package_root_directory))

app = Flask(__name__, template_folder="templates")


@app.route("/")
def home():
    """Homepage"""
    return render_template('index.html', title='Home')


if __name__ == "__main__":
    app.run()
