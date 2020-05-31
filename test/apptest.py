import pytest

from app import create_app, db

a = create_app(config_name='test')

def testindex():
  with a.test_client() as c:
    res = c.get('/')
    self.assertEqual(res.status_code==200)