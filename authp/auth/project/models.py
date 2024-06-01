from flask_login import UserMixin
from . import db
#from sqlalchemy.dialects.postgresql import json

class User(UserMixin, db.Model):
    __tablename__ = 'logins'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(256))
    nome = db.Column(db.String(150))
    
    def __repr__(self):
        return '<User %r>' % self.email
