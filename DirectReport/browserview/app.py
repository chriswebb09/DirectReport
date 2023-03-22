#!/usr/bin/env python3

from flask import Flask, render_template
from DirectReport.models.list_builder import ListBuilder
from flask import Flask, jsonify, request
from DirectReport.database.weekly_storage import DateUUIDTable
from DirectReport.database.entry_storage import DailyEntryStorage

app = Flask(__name__, template_folder="templates")

builder = ListBuilder()


@app.route("/")
def home():
    """Homepage"""
    return render_template('index.html', title='Home')


@app.route("/list")
def list():
    """Homepage"""
    week = builder.list_this_week_as_json()
    return jsonify(week)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run()
