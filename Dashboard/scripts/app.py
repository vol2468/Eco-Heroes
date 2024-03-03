# import os
# from flask import redirect, url_for
# from flask import Flask, render_template

# """ database.py file """
# from flask_sqlalchemy import SQLAlchemy
 


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

# if __name__ == '__main__':
#     app.run()



