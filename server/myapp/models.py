from myapp import db
from sqlalchemy_serializer import SerializerMixin


user_site_table = db.Table('user_site_association',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('site_id', db.Integer, db.ForeignKey('sites.id'), primary_key=True)
)
class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    serialize_rules = ('-sites.user',)

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    reviews = db.relationship('Review', backref='user')

class TouristAttractionSite(db.Model, SerializerMixin):
    __tablename__ = 'sites'

    seralize_rules = ('-user.sites',)
    id = db.Column(db.Integer, primary_key=True)
    touristSite = db.Column(db.String)
    location = db.Column(db.String)
    description = db.Column(db.String)
    rating = db.Column(db.Integer)

    reviews = db.relationship('Review', backref='site')

class Review(db.Model,):
    __tablename__ = "reviews"


    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tourist_attraction_site_id = db.Column(db.Integer, db.ForeignKey('sites.id'))

    User.sites = db.relationship('TouristAttractionSite', secondary=user_site_table, backref=db.backref('users'))
