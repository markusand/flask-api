import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TEST = False

	# JWT AUTHENTICATION
	JWT_SECRET_KEY = 'SUPER_SECRET_PASSWORD'
	JWT_IDENTITY_CLAIM = 'sub'
	JWT_ACCESS_TOKEN_EXPIRES = 1800 # 1800s = 30 minutes
	JWT_REFRESH_TOKEN_EXPIRES = 86400 # 8640s = 1 day

	# SQLALCHEMY
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
	ENV = 'development'
	DEBUG = True

	# SQLAlchemy
	SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'base.db')


class ProductionConfig(Config):
	ENV = 'production'
