from application import *
#from app import *
from flask import json, jsonify
import pytest


def test_index():
  with app.test_client() as c:
    resp=c.get('/index')
    assert b'app.db' in resp.data
    
def test_login():
  u=models.User(username='piotr', email='piotr@mail.com')
  return app.test_client().post('/login', data=dict(username=u.username, email=u.email ), follow_redirects=True)
  

def test_logout():
  with app.test_client() as c:
    return c.get('/logout', follow_redirects=True)


def test_404():
  with app.test_client() as c:
    resp = c.get('/nonexisting')
    assert resp.status_code == 404
    