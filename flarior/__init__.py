from flask.ext.restplus import apidoc
from flask_jwt import JWT


current_app = None


class Flarior(object):
    """
    Flarior app
    """

    jwt = JWT()

    def __init__(self, app=None):
        global current_app
        current_app = self
        self.app = app
        if self.app is not None:
            self.init_app(app)

    def init_app(self, app):
        from api import api_v0
        self.app = app
        self.app.register_blueprint(api_v0, url_prefix='/api/v0')
        self.app.register_blueprint(apidoc.apidoc)

        Flarior.jwt.init_app(app)
