from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    #login_user(user, remember=remember)
    #return redirect(url_for('main.profile'))

    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()
    if user:
        print(user)
    else:
        print('Usuario nao existe, cadastrar')
    
    if not user or not check_password_hash(user.password, password):
        return redirect(url_for('auth.login'))
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))
    
@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    #return redirect(url_for('auth.login'))
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user:
        print(user.name)
    else:
        pass
    
    if user:
        flash('Email ja esta registrado', 'success')
        return redirect(url_for('auth.signup'))
    
    #create a new user
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    
    #add the user to database
    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

