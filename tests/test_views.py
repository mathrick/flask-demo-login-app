from . import FlaskTestCase
from flask import url_for
from flask.ext.login import current_user
from app import db, models, views, forms

class TestSignUp(FlaskTestCase):
    name = "King Arthur"
    email = "arthur@camelot.org"
    password = "asd"
    confirm = "asd"

    def test_sign_up(self):
        rv = self.client.get(url_for("sign_up"))
        assert "<form action=\"/sign-up\" method=\"post\">" in rv.data.lower()

        rv = self.client.post(url_for("sign_up"),
                              data={"name": self.name,
                                    "email": self.email,
                                    "password": self.password,
                                    "confirm": self.confirm})

        self.assert_redirects(rv, url_for('index'))

    def test_login(self):
        rv = self.client.get(url_for("login"))
        assert "<form action=\"/login?next=%2f\" method=\"post\">" in rv.data.lower()

        form = forms.SignUpForm(obj=self)

        views.make_new_user(form)

        with self.client as client:
            # 'with' is needed to access the request for testing
            rv = client.post(url_for("login"), data={"email": self.email,
                                                     "password": self.password,
                                                     "remember": False})
            self.assert_redirects(rv, url_for('index'))
            assert views.get_unread_count()
            assert current_user.is_authenticated()
            
