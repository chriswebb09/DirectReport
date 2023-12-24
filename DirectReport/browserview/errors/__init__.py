from flask import Blueprint
from DirectReport.browserview.errors import handlers


bp = Blueprint('errors', __name__)
