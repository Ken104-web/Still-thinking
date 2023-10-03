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

class GetUsers(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        resp = make_response(
            jsonify(users),
            200,
        )       
        return resp
api.add_resource(GetUsers, '/users')

class GetUserId(Resource):
    def get(self, id):
        each_user = User.query.filter_by(id=id).first()
        if each_user:
            user_data = each_user.to_dict()
            resp = make_response(
                user_data,
                200,
            )
            return resp
        else:
            raise ValueError('User not found')
api.add_resource(GetUserId, '/users/<int:id>')
class GetSites(Resource):
    def get(self):
        sites = [site.to_dict() for site in TouristAttractionSite.query.all()]
        resp = make_response(
            jsonify(sites),
            200,
        )
        return resp
api.add_resource(GetSites, '/sites')

class GetSitesId(Resource):
    def get(self, id):
        each_site = TouristAttractionSite.query.filter_by(id=id).first()
        if each_site:
            user_data = each_site.to_dict()
            resp = make_response(
                user_data,
                200,
            )
            return resp
        else:
            raise ValueError('User not found')
api.add_resource(GetSitesId, '/sites/<int:id>')

class GetReview(Resource):
    def get(self):
        reviews = [review.to_dict() for review in Review.query.all()]
        resp = make_response(
            jsonify(reviews),
            200,
        )
        return resp
class PostReviews(Resource):
    def post(self):
            data = request.get_json()        
            post_review = Review(
                rating = data['String']
            )
            db.session.add(post_review)
            db.session.commit()
            return make_response(post_review.to_dict(), 201)

api.add_resource(GetReview, '/reviews')














