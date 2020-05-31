import unittest
import os
import json

from app import create_app, db

class BucketlistTestCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app(config_name='test')
    self.client=self.app.test_client
    self.bucketlist= {'name':'got for a long holiday'}

    with self.app.app_context():
      db.create_all()

  def test_index(self):
    res = self.client().get('/')
    self.assertEqual(res.status_code==200)

  def test_bucketlist_creation(self):
    res = self.client().post('/bucketlist/', data=self.bucketlist)
    self.assertEqual(res.status_code, 201)
    self.assertIn('holiday', str(res.data))

  def tearDown(self):
    with self.app.app_context():
      db.session.remove()
      db.drop_all()

if __name__=="__main__":
  unittest.main()