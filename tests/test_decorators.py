from . import FlaskTestCase
from werkzeug.datastructures import MIMEAccept, Headers

from app import decorators

class TestDecorators(FlaskTestCase):
    def test_json_result(self):
        assert decorators.json_result

        reject_msg = "This is a JSON API endpoint"

        rv = self.client.get("/")
        assert reject_msg in rv.data and rv.status_code >= 400

        def try_reject(*mime_types):
            accept = MIMEAccept(mime_types)
            rv = self.client.get("/", headers = Headers([('Accept', accept.to_header())]))
            return reject_msg in rv.data and rv.status_code >= 400 and rv.mimetype != "application/json"

        def try_accept(*mime_types):
            accept = MIMEAccept(mime_types)
            rv = self.client.get("/", headers = Headers([('Accept', accept.to_header())]))
            return rv.status_code == 200 and rv.mimetype == "application/json"

        assert try_reject(("*/*", 1))
        assert try_reject(("text/html", 1), ("*/*", 0.8))

        assert try_accept(("application/json", 1), ("*/*", 0.8))
        assert try_accept(("text/html", 1), ("application/json", 0.9), ("*/*", 0.8))
