from flask import Flask, render_template, request
import requests
from index import index

app = Flask(__name__)


@app.route('/')         
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/index', methods=['GET', 'POST'])
def call_index():
    result = index()
    return result




if __name__ == '__main__':
    app.run()
