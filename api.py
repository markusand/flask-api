#!/usr/bin/env python

from flask import Flask
from flask_restplus import Api
from flask_jwt_extended import JWTManager

from config import DevelopmentConfig as config

# Import namespaces
from ns.auth import ns as auth


# Init app and plugins
app = Flask(__name__)
app.config.from_object(config())
api = Api(app)
jwt = JWTManager(app)

# Register namespaces
api.add_namespace(auth)


if __name__ == '__main__':
	app.run()
