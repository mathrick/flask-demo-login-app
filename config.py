import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "db", 'app.db')
    ALEMBIC_MIGRATE_DIR = os.path.join(basedir, "db", 'migrations')

class TestingConfig(Config):
    # Disable error catching
    TESTING = True
    # In-memory DB
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class DevelopmentConfig(Config):
    DEBUG = True
