#!/usr/bin/env python3

from DirectReport.models.list_builder import ListBuilder
from flask import Flask, jsonify, render_template
from DirectReport.database.weekly_storage import DateUUIDTable
from DirectReport.database.entry_storage import DailyEntryStorage

app = Flask(__name__, template_folder="templates")

builder = ListBuilder()


@app.route("/")
def home():
    """Homepage"""
    weekly = DateUUIDTable('SQLite_Python.db')
    print(weekly.list_all_entries())
    return render_template('index.html', title='Home')


@app.route("/list", methods=['GET'])
def list():
    """Homepage"""
    week = jsonify(builder.list_this_week())
    print(week)
    return render_template('index.html', data=week)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404


if __name__ == "__main__":
    app.run()
