
import os
from flask import Flask, request, jsonify, redirect, abort, render_template, url_for

from flask_sqlalchemy import SQLAlchemy



from instance.config import app_config

app = Flask(__name__)

#app.config.from_object(app_config[os.getenv('APP_ENV')])
db = SQLAlchemy()


def create_app(config_name):
  app.config.from_object(app_config[config_name])
  #app.config.from_pyfile('config.py')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)

  
  from app.models import Bucketlist
  @app.route('/')
  def index():
    return render_template('index.html', title='flask template')
    

  @app.route('/bucketlist', methods=['GET', 'POST'])
  def bucketlist():
    if request.method == 'POST':
      name=str(request.data.get('name', ''))
      if name:
        bucketlist=Bucketlist(naem=name)
        buckelist.save()
        response=jsonify({
          'id':bucketlist.id,
          'name': bucketlist.name,
          'created': bucketlist.created,
          'modified':bucketlist.modified
        })

        response.status_code=201
        return response
    else:
      bucketlist = Bucketlist.get_all()
      results=[]
      for b in bucketlist:
        obj={
          'id':b.id,
          'name': b.name,
          'created': b.created,
          'modified':b.modified

        }
        results.append(obj)
        response.status_code =200

        return response


  return app


  

  



