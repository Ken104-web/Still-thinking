from myapp.models import User, TouristAttractionSite, Review
from myapp import db, app
from faker import Faker

fake = Faker()


with app.app_context():
    User.query.delete()
    TouristAttractionSite.query.delete()
    Review.query.delete()

    users = []
    for i in range(20):
        print('**Hello**')
        people = User(username=fake.name())
        users.append(people)
    db.session.add_all(users)
    db.session.commit()


