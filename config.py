import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    TESTING = False
    DEBUG = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = "'tis just a flesh wound!"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "db", 'app.db')
    ALEMBIC_MIGRATE_DIR = os.path.join(basedir, "db", 'migrations')

class TestConfig(Config):
    # Disable error catching
    # TESTING = True
    # In-memory DB
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class DevelopmentConfig(Config):
    DEBUG = True
