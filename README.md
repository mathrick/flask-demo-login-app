Basic login app
===============
This is a simple webapp implementing login functionality, built on Flask and AngularJS. It doesn't really do anything useful as such, but it does implement the meat of what many apps need, ie. sign up, login, and a trivial messaging system between users. If you were writing a serious app, it would very likely pass through a stage much like this.

Installing and running
======================

Pip packages
------------
The easiest way to run and deploy the app is by using python virtualenvs. Make sure you have virtualenv installed, then do the following in terminal (assuming you're running a Unix-like system):

    cd /path/to/checkout/login-flask
    virtualenv _flask
    . _flask/bin/activate
    pip install -r requirements.txt

Other requirements
------------------
For security reasons, the app uses py-bcrypt for password hashing. That module is not in the standard library, and it accesses a C library, which means you will need to have the compiler, as well as C Python headers installed. On Debian/Ubuntu, you can use the following to install them:

    sudo apt-get install python-dev

SQLite3 is used as the DB, so you will need to have that installed and accessible to your Python. Almost all distributions ship and install sqlite by default, so you will likely have it already. But if not, something like

    sudo apt-get install libsqlite3-0

or an equivalent for your distribution should get it.

Running
-------
Assuming everything installed correctly, you can now do:

    ./run.py test

This will launch the test suite. If everything passes, you can now freely run the development server:

    ./run.py

Database setup
-------
The above will give you a running instance, but not actually a working system, since the database in non-test scenarios needs to be explicitly upgraded to the latest schema:

    ./run.py db upgrade

Later on, if you make some changes to the models, you will also need to prepare a migration representing the corresponding changes, and apply it afterwards:

    ./run.py db migrate

    # IMPORTANT: review and edit the created version file to make sure
    # it does what you expect! Alembic is not perfect. Don't forget to
    # commit it either

    ./run.py db upgrade

If you're not familiar with the concept of DB migrations, you can read about it [on Wikipedia](https://en.wikipedia.org/wiki/Schema_migration).

Code
====

Project structure:

        app/
           __init__.py
           views.py
           models.py
           forms.py
           templates/
              ...
           static/
              angular/
              ...
        tests/
           ...
        run.py
        config.py
        requirements.txt
        setup.py

The app is built on the standard MVC model you'd expect, modulo some naming differences.

* `app/` contains the actual application code. 
 * `views.py` would really be called `controllers.py` in most frameworks, but it's most commonly called "views" in Flask.
 * `models.py` contains the DB models, built on SQLAlchemy.
 * `forms.py` contains the WTForms form objects, used to communicate between views functions and templates and to build up models out of submitted data.
 * `__init__.py` is just the application init code.
 * `templates/` holds Jinja2 templates, as expected.
 * `static/` contains all the assets, ie. Javascript and CSS.
  * `angular/` contains AngularJS templates
* `tests/` contains the test suite, which can be run with `run.py`.
* `config.py` contains the Flask app configuration.
* `run.py` is the runner script, implementing a number of commands via Flask-Script. Running it without argument will launch the local development server, `run.py test` will launch the test suite, and `run.py db` has a number of subcommands for creating the database and applying migrations. `run.py --help` will show you all the details.
* `requirements.txt` is a pip requirements file, used for grabbing all the required packages automatically.
* `setup.py` is a setuptools script to prepare a distributable package.

