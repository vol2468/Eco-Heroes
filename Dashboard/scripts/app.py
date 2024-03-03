import os
from flask import redirect, url_for
from flask import Flask, render_template

""" database.py file """
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.debug = True
 
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
 
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)
 
if __name__ == '__main__':
    app.run()

class User(db.Model):
    username = db.Column(db.String(100), primary_key=True, unique=True)
    city = db.Column(db.String(100))
    latitude = db.Column(db.String(100))
    longitude = db.Column(db.String(100))
    point = db.Column(db.Integer())
    level = db.Column(db.Integer())


class sdgs(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    image = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Name : {self.first_name}, Age: {self.age}"

# """ Creating Database with App Context"""
# def create_db():
#     with app.app_context():
#         db.create_all()

# from flask import request

# @app.route("/index.py", methods=['GET', 'POST'])
# def add_vehicle():
#     if request.method == 'POST':
#         name = request.form.get('username')
#         selectedcity = request.form.get('selectedcity')
 
#         add_detail = User(
#             username=name,
#             city=selectedcity
#         )
#         db.session.add(add_detail)
#         db.session.commit()
#         detail=User.query.all()
#         print(detail.username)
#     return redirect(url_for('index'))

# @app.route("/test")
# def test():
#     detail=User.query.all()
#     return render_template(('test.html'), details=detail)

# @app.route('/login.py', methods=['GET', 'POST'])
# def loginCheck():
#     username = request.form.get('username')
#     user = User.query.filter_by(username=username).first()
#     if user:
#         return redirect(url_for('index.html'))
#     else:
#         # Handle invalid username
#         return render_template("login.html")
    
# @app.route('/login')
# def login():
#     return render_template('login.html')

# @app.route('/map')
# def map():
#     return render_template('map.html')

# @app.route('/index')
# def index():
#     return render_template("index.html")

# @app.route('/register')
# def register():
#     return render_template("register.html")
 
# if __name__ == "__main__":
#     from models import User
#     create_db()
#     app.run(debug=True)


# file_path = os.path.abspath(os.getcwd())+"\database.db"
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/joy/Desktop/Projects/Hackathon/Dashboard/instances/project.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# class User(db.Model):
#     username = db.Column(db.String(10), primary_key=True)
#     city = db.Column(db.String(10), nullable=False)
#     latitude = db.Column(db.String(20), nullable=False)
#     longitude = db.Column(db.String(20), unique=True, nullable=False)
#     level=db.Column(db.Integer())

# class sdgs(db.Model):
#     id = db.Column(db.String(10), primary_key=True)
#     image = db.Column(db.String(10), nullable=False)
#     description = db.Column(db.String(20), nullable=False)
#     longitude = db.Column(db.String(20), unique=True, nullable=False)


    # def __repr__(self):
    #     return f'<User {self.username}>'from project_name import app, db