from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import LoginManager, UserMixin, current_user, login_required, logout_user, login_user
import pandas as pd
import matplotlib.pyplot as plt

auth = Blueprint('auth', __name__)

#@auth.route('/login')
#def login():
#    return render_template('login.html')


@auth.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        print(current_user)
        return redirect(url_for('main.profile'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            #user = User(email)
            login_user(user)
            print(email, password)
            return redirect(url_for('main.profile'))
            #return redirect(url_for('dashboard'))
        else:
            flash("Usuario ou senhas invalidos ou nao existe")
    
        if not user or not check_password_hash(user.password, password):
            return redirect(url_for('auth.login'))
        
    return render_template('login.html')

users = {
    'user1': {'id': 1, 'email': 'fabio1@fabio1.com.br', 'data_file': 'users_data/user1.csv'},
    'user2': {'id': 2, 'email': 'fabio@fabio.com.br', 'data_file': 'users_data/user2.json'}
}

@auth.route('/dashboard')
@login_required
def dashboard():
    user_data_file = None
    for email, user in users.items():
        if user['id'] == current_user.id:
            user_data_file = user['data_file']
            break
    print(user_data_file)
    if not user_data_file:
        flash('Nao exitem dados para seu Usuario')
        return render_template('dashboard.html', name=current_user.id, data_available=False)
    #elif current_user.username == 'Guest':
    #    flash('Please login in to see your stream!', 'error')
    #    return redirect(url_for('index'))
    if user_data_file.endswith('.csv'):
        data = pd.read_csv(user_data_file)
    elif user_data_file.endswith('json'):
        data = pd.read_json(user_data_file)
    else:
        data = pd.DataFrame()

    if not data.empty:
        plot = data.plot(kind='bar')
        plt.savefig('static/plot.png')
        plt.close()
    return render_template('dashboard.html', name=current_user.id, data_available=not data.empty)


@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        #return redirect(url_for('auth.login'))
        email = request.form.get('email')
        nome = request.form.get('nome')
        password = request.form.get('password')
    
        user = User.query.filter_by(email=email).first()
        if user:
            print(user.email)
        else:
            pass
    
        if email in user:
            flash('Email ja esta registrado, faca login', 'warning')
            return redirect(url_for('auth.login'))
    
        #create a new user
        new_user = User(email=email, nome=nome, password=generate_password_hash(password, method='pbkdf2:sha1', salt_length=8))
    
        #add the user to database
        db.session.add(new_user)
        db.session.commit()
    
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    if session.get("Voce ja esta logado"):
        del session['voce ja esta logado']
    flash('Voce se desconectou com sucesso', 'success')
    return redirect(url_for('auth.login'))
