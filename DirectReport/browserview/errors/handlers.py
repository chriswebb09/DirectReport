#!/usr/bin/env python3

from flask import render_template, request
from DirectReport.browserview.errors import bp
from DirectReport.browserview.api.errors import error_response as api_error_response


def wants_json_response():
    return request.accept_mimetypes['application/json'] >= request.accept_mimetypes['text/html']


@bp.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 errors (page not found).

    :param e: The error object.
    :return: Rendered HTML template for the 404 error page.
    """
    if wants_json_response():
        print(e)
        return api_error_response(404)
    return render_template('404.html', error=e), 404


@bp.app_errorhandler(500)
def internal_error(error):
    if wants_json_response():
        print(error)
        return api_error_response(500)
    return render_template('500.html', error=error), 500
