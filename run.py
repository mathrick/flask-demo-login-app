#!/usr/bin/env python
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db

migrate = Migrate(app, db, directory=app.config['ALEMBIC_MIGRATE_DIR'])

class MyServer(Server):
    def run(self, *args, **kwargs):
        db.init_app(app)
        super(MyServer, self).run(*args, **kwargs)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run(default_command="runserver")
