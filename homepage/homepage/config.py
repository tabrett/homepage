import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'CHANGE-THIS-LATER'

class ProductionConfig(BaseConfig):
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(BaseConfig):
    TESTING = True