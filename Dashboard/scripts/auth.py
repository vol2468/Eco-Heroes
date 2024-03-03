from flask import Blueprint, render_template, request, flash, redirect, url_for


# <editor-fold desc="Description">
# from .models import User
# from . import db
# from flask_login import login_user, login_required, logout_user, current_user
# </editor-fold>
from scripts.compare import compare

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/goal')
def goal():
    return render_template("goal.html")


@auth.route('/index')
def index():
    return render_template("index.html")


@auth.route('/logout')
def logout():
    return render_template("logout.html")


@auth.route('/register')
def register():
    return render_template("register.html")

@auth.route('/map')
def map():
    return render_template('map.html')


@auth.route('/compare.py', methods=['GET', 'POST'])
def call_compare():
    result = compare()
    return result






"""
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Logged in successfully!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash('Username does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.', category='error')
        elif len(username) < 4:
            flash('Username must be greater than 3 characters.', category='error')
        else:
            new_user = User(username=username, method='sha256')
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
"""""
