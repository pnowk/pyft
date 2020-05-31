
from datetime import datetime
from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(50), index=True, unique=True)
  email=db.Column(db.String(130), index=True, unique=True)
  password=db.Column(db.String(128))
  
  
  logins=db.relationship('UserLogin', backref='user', lazy='dynamic')

  def __repr__(self):
    classname=type(self).__name__
    return '{}({}, {})'.format(classname, self.username, self.email)


class UserLogin(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  timestamp=db.Column(db.DateTime, index=True, default=datetime.utcnow)
  userid = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return '{}({}, {})'.format(type(self).__name__, self.userid, self.timestamp)
