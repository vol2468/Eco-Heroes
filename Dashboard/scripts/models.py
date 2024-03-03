import sqlalchemy as db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    username = db.Column(db.String(100), primary_key=True, unique=True)
    city = db.Column(db.String(100))
    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))


class SDG(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    image = db.Column()
    desc = db.Column(db.String(1000))
    orgName = db.Column(db.String(100))
    ordLogo = db.Column()
    orgLink = db.Column(db.String(300))
