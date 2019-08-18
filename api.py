#!/usr/bin/env python

from flask import Flask
from flask_restplus import Api
from flask_jwt_extended import JWTManager

from config import DevelopmentConfig as config
from db import db

# Import namespaces
from ns.auth import ns as auth
from ns.users import ns as users


# Init app and plugins
app = Flask(__name__)
app.config.from_object(config())
app.app_context().push()
api = Api(app)
jwt = JWTManager(app)
db.init_app(app)

# Register namespaces
api.add_namespace(auth)
api.add_namespace(users)


if __name__ == '__main__':
	app.run()
