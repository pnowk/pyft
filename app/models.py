
from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



class Bucketlist(db.Model):
  __tablename__ = "bucketlist"

  id = db.Column(db.Integer, primary_key=True)
  name=db.Column(db.String(255))
  created=db.Column(db.DateTime, default=datetime.utcnow())
  modified=db.Column(
    db.DateTime, default=datetime.utcnow(),
    onupdate=datetime.utcnow()
  
  )

  def __init__(self, name):
    self.name=name
  
  def save(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_all(cls):
    return cls.query.all()

  
  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    clsname=type(self).__name__
    return '{}({})'.format(clsname, self.name)

    



class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username=db.Column(db.String(50), index=True, unique=True)
  email=db.Column(db.String(130), index=True, unique=True)
  password=db.Column(db.String(128))

  tasks=db.relationship('Task', backref='user', lazy='dynamic')

  def set_password(self, password):
    self.password=generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)
  
  def __repr__(self):
    classname=type(self).__name__
    return '{}({}, {})'.format(classname, self.username, self.email)


class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title=db.Column(db.String(50), index=True, unique=True)
  description=db.Column(db.String(50), index=True, unique=True)
  status=db.Column(db.Boolean(), default=False)
  userid = db.Column(db.Integer, db.ForeignKey('user.id'))

  def __repr__(self):
    return '{}({}, {})'.format(type(self).__name__, self.taskname, self.userid)