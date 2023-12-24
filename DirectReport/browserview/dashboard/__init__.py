#!/usr/bin/env python3

from flask import Blueprint

bp = Blueprint('dashboard', __name__)

from DirectReport.browserview.dashboard import routes
