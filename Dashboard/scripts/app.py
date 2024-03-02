from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/index', methods=['GET', 'POST'])
def index():
    searchword = request.args.get('key', '')
    return render_template('compare.html', name=searchword)

if __name__ == '__main__':
    app.run()
