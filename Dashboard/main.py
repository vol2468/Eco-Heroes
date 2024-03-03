from flask import Flask, render_template, Blueprint
from scripts import create_app
from flask_sqlalchemy import SQLAlchemy

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)



"""



@app.route('/')         
def home():  # put application's code here
    return 'Hello World!'


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
"""

# @app.route('/login')
# def login():
#     return render_template('login.html')

