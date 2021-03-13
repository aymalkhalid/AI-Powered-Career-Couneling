#Table 1
#user can ask and answer question. 
#Admin who can give rights to certain user to become expert and answer questions.

#Table 2
# Containing  The actual Question and Answers.
from .extensions import db
# for adding functionality to user model or route
from flask_login import UserMixin
#to generate passowrd hashing
from werkzeug.security import generate_password_hash
from datetime import datetime
#-------------Accessing DataBase Command---------------------

#sqlite3 flask_qa/db.sqlite3 
class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    name = db.Column(db.String(50), index=True, unique=True)
    password=db.Column(db.String(100))
    email = db.Column(db.String(120), index=True, unique=True)
    expert=db.Column(db.Boolean)
    admin=db.Column(db.Boolean)
#all questions asked by user;
    questions_asked = db.relationship(
        'Question',
         foreign_keys='Question.asked_by_id',
         backref='asker',lazy=True)
#all questions requested by user to be answered;
    answers_requested = db.relationship(
        'Question',
        foreign_keys='Question.expert_id',
        backref='expert',
        lazy=True
   )
   #The __repr__ method tells Python how to print objects of this class, which is going to be useful for debugging.
    def __repr__(self):
        return '<User {}>'.format(self.username) 

    @property
    def unhashed_password(self):
        raise AttributeError("Cannot View Unhashed Password")
    
    #setting Password
    @unhashed_password.setter
    def unhashed_password(self,unhashed_password):
        self.password = generate_password_hash(unhashed_password)


class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True,unique=True)
    question = db.Column(db.Text,unique=True)
    answer = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    asked_by_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    expert_id = db.Column(db.Integer, db.ForeignKey('user.id'))