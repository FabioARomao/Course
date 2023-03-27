from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
import requests

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
    #return 'Index'

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.name)

@main.route('/callback')
@login_required
def callback():
    #return render_template('callback.html', name=current_user.name)
    language = request.args.get('language')

    return '''<h1>The language value is: {}</h1>'''.format(language)    