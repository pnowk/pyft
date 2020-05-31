

from flask import render_template, flash, redirect

from app import app

from app.forms import LoginForm
import pytest

@app.route('/')
@app.route('/index')
def index():
  data = {'config': app.config}
  return render_template('index.html', title='Home', data=data)


@app.route('/login', methods=['GET', 'POST'])
def login():
  form=LoginForm()
  if form.validate_on_submit():
    flash('Login requested for user {}'.format(form.username.data))
    return redirect('/index')
  
  return render_template('login.html', title='SignIn', form=form)
  