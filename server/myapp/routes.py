from flask import make_response, jsonify, request
from myapp import db, app
from flask_restful import Resource, Api
from myapp.models import User, TouristAttractionSite, Review


api = Api(app)
class Home(Resource):
    def get(self):
        resp_dict = {
            "Home": "Welcome to Tour guide"
        }
        resp = make_response(
            jsonify(resp_dict),
            200,
        )
        return resp
api.add_resource(Home, '/')


