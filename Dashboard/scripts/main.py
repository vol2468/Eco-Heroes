from flask import Flask, render_template
from compare import compare

app = Flask(__name__)


@app.route('/')         
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/index')         
def index():
    return render_template('index.html')

@app.route('/map.html')         
def map():
    return render_template('map.html')

@app.route('/compare.py', methods=['GET', 'POST'])
def call_compare():
    result = compare()
    return result


if __name__ == '__main__':
    app.run()
