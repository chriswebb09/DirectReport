#!/usr/bin/env python3

from DirectReport.models.list_builder import ListBuilder
from flask import Flask, jsonify, render_template
from DirectReport.database.weekly_storage import WeekUUIDTable
from DirectReport.database.entry_storage import DailyEntryStorage
import json

app = Flask(__name__, template_folder="templates")

builder = ListBuilder()


@app.route("/")
def home():
    """Homepage"""
    # weekly = DateUUIDTable('SQLite_Python.db')
    # print(weekly.list_all_entries())
    items = DailyEntryStorage('SQLite_Python.db')
    # print(items.get_all_entries())
    # list = jsonify(builder.list_this_week_as_json())
    # print(list)
    print(items.get_all_entries())
    return render_template('index.html', title='Home', data=[])


@app.route("/list", methods=['GET'])
def list():
    """Homepage"""
    items = DailyEntryStorage('SQLite_Python.db')
    week = items.get_all_entries_json()
    # print(week)
    # return week
    weekitem = json.dumps(week, indent=5)
    print(weekitem)
    print(jsonify(weekitem))
    return render_template('list.html', title='List', data=week)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404


if __name__ == "__main__":
    app.run()
