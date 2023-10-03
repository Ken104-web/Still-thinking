from myapp import db

user_site_table = db.Table('user_site_association',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('site_id', db.Integer, db.ForeignKey('sites.id'))
)
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    reviews = db.relationship('Review', backref='user')

class TouristAttractionSite(db.Model):
    __tablename__ = 'sites'

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String)
    description = db.Column(db.String)
    rating = db.Column(db.Integer)

    reviews = db.relationship('Review', backref='site')

class Review(db.Model):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tourist_attraction_site_id = db.Column(db.Integer, db.ForeignKey('sites.id'))

    User.sites = db.relationship('TouristAttractionSite', secondary=user_site_table, backref=db.backref('users'))
