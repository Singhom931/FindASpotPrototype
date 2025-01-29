from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_caching import Cache
import imaplib

db = SQLAlchemy()
mail_smtp = Mail()
cache = Cache(config={'CACHE_TYPE': 'simple'})
mail_imap = imaplib.IMAP4_SSL("imap.gmail.com")

# User model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
  
class Payment(db.Model):
    __tablename__ = 'payments'
    email = db.Column(db.String(120), primary_key=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)   
    date = db.Column(db.String(120), nullable=False)
    number = db.Column(db.String(120), nullable=False)