from flask import Flask, redirect, request,url_for,render_template
import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

def create_app():
    app = Flask(__name__)
    return app