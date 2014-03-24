import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "db", 'app.db')
ALEMBIC_MIGRATE_DIR = os.path.join(basedir, "db", 'migrations')
