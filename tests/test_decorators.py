from . import FlaskTestCase
from werkzeug.datastructures import MIMEAccept, Headers

from app import decorators

class TestDecorators(FlaskTestCase):
    def test_decorator_json_result(self):
        assert decorators.json_result

        reject_msg = "This is a JSON API endpoint"

        rv = self.client.get("/")
        assert reject_msg in rv.data

        def try_accept(*mime_types):
            accept = MIMEAccept(mime_types)
            return reject_msg not in self.client.get("/", headers = Headers([('Accept', accept.to_header())])).data

        assert not try_accept(("*/*", 1))
        assert not try_accept(("text/html", 1), ("*/*", 0.8))

        assert try_accept(("application/json", 1), ("*/*", 0.8))
        assert try_accept(("text/html", 1), ("application/json", 0.9), ("*/*", 0.8))
