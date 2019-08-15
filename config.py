class Config(object):
	DEBUG = False
	TEST = False

	# JWT AUTHENTICATION
	JWT_SECRET_KEY = 'SUPER_SECRET_PASSWORD'
	JWT_IDENTITY_CLAIM = 'sub'
	JWT_ACCESS_TOKEN_EXPIRES = 1800 # 1800s = 30 minutes
	JWT_REFRESH_TOKEN_EXPIRES = 86400 # 8640s = 1 day


class DevelopmentConfig(Config):
	ENV = 'development'
	DEBUG = True


class ProductionConfig(Config):
	ENV = 'production'
