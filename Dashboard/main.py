from flask import Flask, render_template, Blueprint
from scripts import create_app


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)


