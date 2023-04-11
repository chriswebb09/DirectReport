#!/usr/bin/env python3

from DirectReport.models.list_builder import ListBuilder
from flask import Flask, render_template, redirect
from DirectReport.database.entry_storage import EntryStorage

app = Flask(__name__, template_folder="templates")

builder = ListBuilder()


@app.route("/")
def home():
    """Homepage"""
    return render_template('index.html', title='Home', data=[])


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404


@app.route("/list", methods=['GET', 'POST'])
def list():
    items = EntryStorage('SQLite_Python.db')
    week = items.get_all_entries_json()
    return render_template('list.html', title='List', data=week)



@app.route('/entry/<id>', methods=['GET'])
def detail(id=None):
    item = EntryStorage('SQLite_Python.db')
    entry = item.get_entry(id).to_dict()
    return render_template('detail.html', title='Detail', data=entry)


@app.route('/delete/<id>', methods=['GET'])
def delete(id=None):
    item = EntryStorage('SQLite_Python.db')
    item.delete_entry(id)
    return redirect("/list", code=302)


if __name__ == "__main__":
    app.run()
