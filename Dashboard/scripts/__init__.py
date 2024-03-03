from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'r'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db=SQLAlchemy(app)

    class User(db.Model, UserMixin):
        username = db.Column(db.String(100), primary_key=True, unique=True)
        city = db.Column(db.String(100))
        lat = db.Column(db.String(100))
        lon = db.Column(db.String(100))

    def __init__(self, username, city, lat, lon):
        self.name = username
        self.city = city
        self.lat = lat
        self.lon = lon

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # from .models import User

    # db.create_all()

    with app.app_context():
        db.create_all()

    return app


"""
def create_database(app):
    if not path.exists('Dashboard/scripts/' + DB_NAME):
        db.create_all()
        print("Created Database!")
"""