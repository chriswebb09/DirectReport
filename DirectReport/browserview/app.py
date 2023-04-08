#!/usr/bin/env python3

from DirectReport.models.list_builder import ListBuilder
from flask import Flask, render_template
from DirectReport.database.entry_storage import DailyEntryStorage

app = Flask(__name__, template_folder="templates")

builder = ListBuilder()


@app.route("/")
def home():
    """Homepage"""
    return render_template('index.html', title='Home', data=[])


@app.route("/list", methods=['GET'])
def list():
    """Homepage"""
    items = DailyEntryStorage('SQLite_Python.db')
    week = items.get_all_entries_json()
    return render_template('list.html', title='List', data=week)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404


if __name__ == "__main__":
    app.run()
