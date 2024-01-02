#!/usr/bin/env python3

from flask_login import login_required, current_user
from DirectReport.models.report.report_builder import ReportBuilder
from DirectReport.browserview.api import bp

@bp.route("/reports/list", methods=['GET'])
@login_required
def get_list():
    reports = ReportBuilder.get_reports_for_user_id(current_user.id)
    return reports, 201
