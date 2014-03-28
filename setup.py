from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests']
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(version='0.1',
      name='login',
      description='Simple Flask-based login service',
      packages=['app'],
      install_requires=[
          # Flask is kinda crucial :)
          'Flask==0.10.1',

          # Other libs we explicitly used
          'Flask-SQLAlchemy==1.0',
          'Flask-WTF==0.9.5',
          'SQLAlchemy==0.9.3',
          'Flask-Migrate==1.2.0',
          'Flask-Script==0.6.7',
          'Flask-Testing==0.4.1',
          'Flask-Bcrypt==0.5.2',
          'Flask-Login==0.2.10',
          'Flask-RESTful==0.2.12',
          'pytest==2.5.2',

          # Automatic deps as brought in when I pip installed Flask
          'Jinja2==2.7.2',
          'MarkupSafe==0.19',
          'Werkzeug==0.9.4',
          'argparse==1.2.1',
          'itsdangerous==0.23',
          'wsgiref==0.1.2',
          'py==1.4.20',

          # Other automatic deps
          'Tempita==0.5.2',
          'WTForms==1.0.5',
          'decorator==3.4.0',
          'pbr==0.7.0',
          'six==1.6.1',
          'Mako==0.9.1',
          'alembic==0.6.3',
          'py-bcrypt==0.4',
          'aniso8601==0.82',
          'pytz==2014.2',
      ],
      tests_require=['pytest'],
      cmdclass = {'test': PyTest},
)
