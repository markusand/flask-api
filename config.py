class Config(object):
  DEBUG = False
  TEST = False

class DevelopmentConfig(Config):
  ENV = 'development'
  DEBUG = True

class ProductionConfig(Config):
  ENV = 'production'
