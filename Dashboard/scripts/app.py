from flask import Flask, render_template
from compare import compare

app = Flask(__name__)


@app.route('/')         
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/index')         
def index():
    return render_template('index.html')

@app.route('/map')         
def map():
    return render_template('map.html')

@app.route('/compare.py', methods=['GET', 'POST'])
def call_compare():
    result = compare()
    return result




# @app.route('/login')         
# def login():
#     return render_template('login.html')




# @app.route('/login')
# def login():
#     return render_template('login.html')

if __name__ == '__main__':
    app.run()
