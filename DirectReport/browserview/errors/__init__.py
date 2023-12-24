#!/usr/bin/env python3

from flask import Blueprint

bp = Blueprint('errors', __name__)

from DirectReport.browserview.errors import handlers
