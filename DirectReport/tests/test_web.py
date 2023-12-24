#!/usr/bin/env python3

import sys
from pathlib import Path
from DirectReport.browserview import create_app


file = Path(__file__).resolve()
package_root_directory = file.parents[1]
sys.path.append(str(package_root_directory))

sys.path.append('.')


# def test_index_route():
#     app = create_app()
#     response = app.test_client().get('/')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8').__contains__('<meta charset="utf-8"/>')
#
#
# def test_list_route():
#     app = create_app()
#     response = app.test_client().get('/list')
#     assert response.status_code == 302
#
#
# def test_404_route():
#     app = create_app()
#     response = app.test_client().get('/wiki')
#     assert response.status_code == 404
#     assert response.data.decode('utf-8').__contains__('404')
