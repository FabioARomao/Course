from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import current_user, login_required, logout_user, login_user

auth = Blueprint('auth', __name__)

#@auth.route('/login')
#def login():
#    return render_template('login.html')

@auth.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.profile'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #remember = True if request.form.get('remember') else False
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            print(email, password)
            return redirect(url_for('main.profile'))
            #return redirect(url_for('dashboard'))
        else:
            flash("Usuario ou senhas invalidos ou nao existe")
    
        if not user or not check_password_hash(user.password, password):
            return redirect(url_for('auth.login'))
        
    return render_template('login.html')
    
#@auth.route('/signup')
#def signup():
#    return render_template('signup.html')

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
    
        if user:
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

@auth.route('/usuarios', methods = ['GET'])
def usuario():
    users = User.query.all()
    print(type(users))
    user_list = [{"nome": user.nome, "email": user.email} for user in users] #inserir no for , "data_file": user.data_file
    print(user_list)
    #del[user_list]['nome':'']
    return render_template('usuario.html', users=user_list)
