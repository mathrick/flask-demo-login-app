from flask import json, request, Response

def _request_wants_json():
    types = request.accept_mimetypes
    return (types['application/json'] > 0 and
            # Most browsers pass */* in Accept:, we don't want to match that
            'application/json' in types.values())

def json_result(fun):
    """
    Decorator to JSONify responses automatically for API endpoints. It checks if
    the request accepts \'application/json\' and if so, automatically calls
    flask.json.jsonify on the result of the decorated function. Otherwise a 415
    HTTP status with a short message is returned.
    """
    def decorated(*args, **kwargs):
        if _request_wants_json():
            return json.jsonify(**fun(*args, **kwargs))
        else:
            return Response("""This is a JSON API endpoint. It should not be viewed directly in a browser.
Please retry your request with 'application/json' in the Accept: header.""",
                            status=415, mimetype="text/plain")
    return decorated
