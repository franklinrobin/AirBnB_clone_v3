#!/usr/bin/python3
'''
Index File
'''

from flask import jsonify
from api.v1.views import app_views
from api.v1.app import storage
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity

classes = {'states': State,
           'cities': City,
           'users': User,
           'places': Place,
           'reviews': Review,
           'amenities': Amenity}


@app_views.route('/status')
def status_route():
    '''returns a JSON status info'''
    data = {
            "status": "OK"
            }
    return jsonify(data)


@app_views.route('/stats')
def count_objects():
    '''retrieves the number of each objects by type'''
    stats = {}
    for k, v in classes.items():
        amount = storage.count(v)
        stats[k] = amount
    return jsonify(stats)
