#!/usr/bin/env python

from flask import Flask
from flask_restplus import Api, Resource
from config import DevelopmentConfig as config

app = Flask(__name__)
app.config.from_object(config())
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
  def get(self):
    return 'Hello world!'

if __name__ == '__main__':
  app.run()
