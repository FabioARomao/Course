from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from .models import User
import os
from . import leitura


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
    #return 'Index'

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.nome)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.nome)

@main.route('/usuarios')
#login_required
def usuario():
    language = request.args.get('language')
    nomes = leitura.leitura_de_arquivo("babys.json")
    html_nomes = ""
    for nome in nomes:
        html_nomes += "<h1>{}</h1>".format(nome)
    return render_template('usuario.html', html_nomes)   
    #return html_nomes
    #return render_template('usuario.html', name=current_user.nome)

@main.route('/usuarios1', methods = ['GET'])
#@login_required
def usuario1():
    users = User.query.all()
    print(type(users))
    user_list = [{"nome": user.nome, "email": user.email} for user in users] #inserir no for , "data_file": user.data_file
    print(user_list)
    #del[user_list]['nome':'']
    return render_template('usuario.html', users=user_list)

@main.route('/callback')
@login_required
def callback():
    language = request.args.get('language')
    nomes = leitura.leitura_de_arquivo("babys.json")
    html_nomes = ""
    for nome in nomes:
        html_nomes += "<h1>{}</h1>".format(nome)
    return html_nomes

@main.route('/callback2')
@login_required
def callback2():
    language = request.args.get('language')
    nomes = User.query.all()
    html_nomes = ""
    for nome in nomes:
        html_nomes += "<h1>{}</h1>".format(nome)
    print(html_nomes)    
    return html_nomes

