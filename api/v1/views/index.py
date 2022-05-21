#!/usr/bin/python3
'''
Index File
'''

import flask
from api.v1.views import app_views


@app_views.route('/status')
def status_route():
    '''returns a JSON status info'''
    data = {
            "status": "OK"
            }
    return flask.jsonify(data)
