from flask import Blueprint

bp = Blueprint('main', __name__)

from DirectReport.browserview.main import routes