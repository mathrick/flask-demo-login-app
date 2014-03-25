from . import FlaskTestCase
from werkzeug.datastructures import MIMEAccept, Headers

from app import decorators

class TestDecorators(FlaskTestCase):
    url="/api/test"
    def test_json_decorator_defined(self):
        self.assertTrue(decorators.json_result)

    def test_json_rejects_html_clients(self):
        reject_msg = "This is a JSON API endpoint"
        
        rv = self.client.get(self.url)
        self.assertTrue(reject_msg in rv.data and rv.status_code >= 400)

        def try_reject(*mime_types):
            accept = MIMEAccept(mime_types)
            rv = self.client.get(self.url, headers = Headers([('Accept', accept.to_header())]))
            return reject_msg in rv.data and rv.status_code >= 400 and rv.mimetype != "application/json"

        self.assertTrue(try_reject(("*/*", 1)))
        self.assertTrue(try_reject(("text/html", 1), ("*/*", 0.8)))
        
    def test_json_decorator_returns_json(self):
        def try_accept(*mime_types):
            accept = MIMEAccept(mime_types)
            rv = self.client.get(self.url, headers = Headers([('Accept', accept.to_header())]))
            return rv.json

        self.assertTrue(try_accept(("application/json", 1), ("*/*", 0.8)))
        self.assertTrue(try_accept(("text/html", 1), ("application/json", 0.9), ("*/*", 0.8)))
