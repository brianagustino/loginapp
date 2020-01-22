import os
import MySQLdb
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    APP_PORT = 4242
    TEMPLATES_AUTO_RELOAD = True


class LocalConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    APP_PORT = 4000
    BASE_API_URL = '/api'
    DB_URL ='mysql+pymysql://root:@localhost:3306/belajar'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    APP_PORT = 4230
    BASE_API_URL = '/api'
    DB_URL ='mysql+pymysql://root:@localhost:3306/belajar'


class ProductionConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    APP_PORT = 4231
    BASE_API_URL = '/api'
    DB_URL ='mysql+pymysql://root:@localhost:3306/belajar'

