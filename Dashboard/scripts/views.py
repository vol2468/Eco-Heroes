from flask import Blueprint, request, flash, render_template
from flask_login import login_required, current_user
import json

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("index.html")

