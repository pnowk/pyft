import os

from app import create_app

os.environ['APPENV'] = 'dev'

config_name=os.getenv('APPENV')

app = create_app(config_name)

if __name__ == "__main__":
  app.run()