import os, sys

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
  ENV='debug'
  DEBUG=True
  TESTING=True
  PORT=33507
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretkeytomyapp'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
      'sqlite:///'+os.path.join(basedir, 'data.db')
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  


class DevConfig(Config):
  DEBUG=True
  ENV='development'
  SQLALCHEMY_DATABASE_URI =  'sqlite:///'+os.path.join(basedir, 'datadev.db')

class TestConfig(Config):
  ENV='testing'
  TESTING=True
  DEBUG=True
  SQLALCHEMY_DATABASE_URI =  'sqlite:///'+os.path.join(basedir, 'datatest.db')


class ProdConfig(Config):
  ENV='production'
  DEBUG=False
  TESTING=False



app_config = {
  'dev':DevConfig,
  'test': TestConfig,
  'prod': ProdConfig


}