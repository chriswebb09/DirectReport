#!/usr/bin/env python3

from flask import Blueprint

bp = Blueprint('auth', __name__)

from DirectReport.browserview.auth import routes
