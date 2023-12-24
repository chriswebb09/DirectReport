from flask import Blueprint

bp = Blueprint('api', __name__)

from DirectReport.browserview.api import auth, errors, reports
