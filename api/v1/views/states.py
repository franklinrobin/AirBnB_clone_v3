#!/usr/bin/python3
'''
Create a new view for State objects that handles
all default RESTFul API actions
'''
import flask
from flask import request, abort
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route("/states", defaults={'state_id': None}, strict_slashes=False,
                 methods=["GET", "POST", "DELETE", "PUT"])
@app_views.route("/states/<state_id>", strict_slashes=False,
                 methods=["GET", "POST", "DELETE", "PUT"])
def http_methods(state_id):
    '''
    Handle the HTTP Methods
    '''
    print('Haru Best')
    if state_id is None:
        if request.method == "GET":
            d = []
            states = storage.all("State")
            for state in states.values():
                d.append(state.to_dict())
            return flask.jsonify(d)

        if request.method == "POST":
            data = request.get_json()
            if type(data) is not dict:
                abort(400, message='Not a JSON')
            if not data['name']:
                abort(400, message='Missing name')
            new_state = State(**data)
            new_state.save()
            return flask.jsonify(new_state.to_dict()), 201

    else:
        if request.method == "GET":
            state = storage.get("State", state_id)
            if not state:
                return abort(404)
            return state.to_dict()

        if request.method == "PUT":
            d_state = storage.get("State", state_id)
            if not d_state:
                return abort(404)
            n_data = request.get_json()
            if type(n_data) is not dict:
                abort(400, message='Not a JSON')
            for key, value in n_data.items():
                if key not in ["id", "state_id", "created_at", "updated_at"]:
                    setattr(d_state, key, value)
            storage.save()
            return flask.jsonify(d_state.to_dict()), 200

        if request.method == "DELETE":
            d_data = storage.get("State", state_id)
            if not d_data:
                return abort(404)
            storage.delete(d_data)
            storage.save()
            return {}, 200
