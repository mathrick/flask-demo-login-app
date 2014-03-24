#!/usr/bin/env python
from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db
import unittest

migrate = Migrate(app, db, directory=app.config['ALEMBIC_MIGRATE_DIR'])

# Wire up the DB for normal server run
class MyServer(Server):
    def run(self, *args, **kwargs):
        db.init_app(app)
        super(MyServer, self).run(*args, **kwargs)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', MyServer)

# Run the testsuite instead of the normal server
@manager.command
def test():
    t = unittest.defaultTestLoader.discover(".")
    runner = unittest.runner.TextTestRunner()
    runner.run(t)

if __name__ == "__main__":
    manager.run(default_command="runserver")
