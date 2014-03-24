#!/usr/bin/env python
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db
from config import ALEMBIC_MIGRATE_DIR

migrate = Migrate(app, db, directory=ALEMBIC_MIGRATE_DIR)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run(default_command="runserver")
