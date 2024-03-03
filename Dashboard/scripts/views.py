from flask import Blueprint #, request, flash, render_template
# from flask_login import login_required, current_user
# from .models import User
# from . import db
# import json

views = Blueprint('views', __name__)


@views.route('/')
# @login_required
def home():
    # if request.method == 'POST':
    #     username = request.form.get('username')#Gets the note from the HTML
    #     city = request.form.get('city')

    #     new_user = User(username=username, city=city)  #providing the schema for the note
    #     db.session.add(new_user) #adding the note to the database
    #     db.session.commit()
    #     flash('User added!', category='success')
    #     return render_template("index.html", user=current_user)
    return "<h1>Test</h1>"

