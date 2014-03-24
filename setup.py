from setuptools import setup

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

          # Automatic deps as brought in when I pip installed Flask
          'Jinja2==2.7.2',
          'MarkupSafe==0.19',
          'Werkzeug==0.9.4',
          'argparse==1.2.1',
          'itsdangerous==0.23',
          'wsgiref==0.1.2',

          # Other automatic deps
          'Tempita==0.5.2',
          'WTForms==1.0.5',
          'decorator==3.4.0',
          'pbr==0.7.0',
          'six==1.6.1',
          'Mako==0.9.1',
          'alembic==0.6.3',
      ],
      test_suite="tests",
  )
