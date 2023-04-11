#!/usr/bin/env python3

from DirectReport.models.list_builder import ListBuilder
from flask import Flask, render_template, redirect
from DirectReport.database.entry_storage import EntryStorage

app = Flask(__name__, template_folder="templates")

builder = ListBuilder()


@app.route("/")
def home():
    """
    Renders the homepage of the web application.

    :return: Rendered HTML template for the homepage.
    """
    return render_template('index.html', title='Home')


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors (page not found).

    :param e: The error object.
    :return: Rendered HTML template for the 404 error page.
    """
    return render_template('404.html', error=e)


@app.route("/list", methods=['GET', 'POST'])
def list():
    """
    Retrieves and renders the list of all entries.

    :return: Rendered HTML template for the list page.
    """
    items = EntryStorage('SQLite_Python.db')
    week = items.get_all_entries_json()
    return render_template('list.html', title='List', data=week)


@app.route('/entry/<id>', methods=['GET'])
def detail(id=None):
    """
    Retrieves and renders the details of a specific entry.

    :param id: The ID of the entry to display.
    :return: Rendered HTML template for the entry details page.
    """
    item = EntryStorage('SQLite_Python.db')
    entry = item.get_entry(id).to_dict()
    return render_template('detail.html', title='Detail', data=entry)


@app.route('/delete/<id>', methods=['GET'])
def delete(id=None):
    """
    Deletes a specific entry and redirects to the list page.

    :param id: The ID of the entry to delete.
    :return: Redirects to the '/list' route.
    """
    item = EntryStorage('SQLite_Python.db')
    item.delete_entry(id)
    return redirect("/list", code=302)


if __name__ == "__main__":
    app.run()
