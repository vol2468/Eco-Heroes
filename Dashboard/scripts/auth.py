from flask import Blueprint, render_template, request, flash, redirect, url_for
from scripts.compare import compare
import sqlite3

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return render_template("index.html")
    


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
#     if request.method == 'POST':
#         username = request.form.get('username')
#         city = request.form.get('city')
#         connection = sqlite3.connect('database.db')
#         cursor = connection.cursor()

#         # Insert images and descriptions into the sdgs table
#         cursor.execute("INSERT INTO kids (username, city) VALUES (?, ?, ?, ?)", (username, city, 0, 0))

#         flash('Logged in successfully!', category='success')

#         # Commit changes and close connection
#         connection.commit()
#         connection.close()
    return render_template("register.html")

@auth.route('/map')
def map():
    return render_template('map.html')


@auth.route('/compare.py', methods=['GET', 'POST'])
def call_compare():
    result = compare()
    return result


@auth.route('/info')
def info():
    return render_template("info.html")


@auth.route('/quiz')
def quiz():
    return render_template('quiz.html')

@auth.route('/quiz1')
def quiz1():
    return render_template('quiz_1.html')

@auth.route('/quiz2')
def quiz2():
    return render_template('quiz_2.html')

@auth.route('/quiz3')
def quiz3():
    return render_template('quiz_3.html')

@auth.route('/quiz4')
def quiz4():
    return render_template('quiz_4.html')

@auth.route('/quiz5')
def quiz5():
    return render_template('quiz_5.html')

@auth.route('/quiz6')
def quiz6():
    return render_template('quiz_6.html')

@auth.route('/quiz7')
def quiz7():
    return render_template('quiz_7.html')

@auth.route('/quiz8')
def quiz8():
    return render_template('quiz_8.html')

@auth.route('/quiz9')
def quiz9():
    return render_template('quiz_9.html')

@auth.route('/quiz10')
def quiz10():
    return render_template('quiz_10.html')

@auth.route('/quiz11')
def quiz11():
    return render_template('quiz_11.html')

@auth.route('/quiz12')
def quiz12():
    return render_template('quiz_12.html')

@auth.route('/quiz13')
def quiz13():
    return render_template('quiz_13.html')

@auth.route('/quiz14')
def quiz14():
    return render_template('quiz_14.html')

@auth.route('/quiz15')
def quiz15():
    return render_template('quiz_15.html')

@auth.route('/quiz16')
def quiz16():
    return render_template('quiz_16.html')

@auth.route('/goal1')
def goal1():
    return render_template('goal1.html')
@auth.route('/goal2')
def goal2():
    return render_template('goal2.html')
@auth.route('/goal3')
def goal3():
    return render_template('goal3.html')

@auth.route('/goal4')
def goal4():
    return render_template('goal4.html')

@auth.route('/goal5')
def goal5():
    return render_template('goal5.html')

@auth.route('/goal6')
def goal6():
    return render_template('goal6.html')






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
