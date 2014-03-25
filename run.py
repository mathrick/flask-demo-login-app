#!/usr/bin/env python
from flask.ext.script import Manager, Server, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from app import app, db, models, views
import pytest

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
@manager.option('-v','--verbose','-e', '--echo', dest='echo',
                default=False, action='store_true',
                help="Echo generated SQL to stderr")
def test(echo):
    if echo:
        app.config['SQLALCHEMY_ECHO'] = True
    pytest.main('tests')

# Set up imports for the 'shell' command
def _make_context():
    return dict(app=app, db=db, models=models, views=views)
manager.add_command("shell", Shell(make_context=_make_context))

if __name__ == "__main__":
    manager.run(default_command="runserver")
