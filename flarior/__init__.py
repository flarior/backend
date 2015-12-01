from flask import Blueprint
from flask_restplus import apidoc
from flask_cors import CORS
from flask_jwt import JWT


current_app = None


class Flarior(object):
    """
    Flarior app
    """

    api = None
    blueprint = None
    jwt = JWT()
    cors = CORS()

    def __init__(self, app=None):
        global current_app
        current_app = self
        self.app = app
        if self.app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        self.jwt.init_app(app)
        self.blueprint = Blueprint(
            'onelove',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path='/static/onelove',
        )
        self.app.register_blueprint(self.blueprint)

        from api import api_v0, api
        self.api = api
        self.app.register_blueprint(api_v0)
        self.app.register_blueprint(apidoc.apidoc)

    @jwt.authentication_handler
    def authenticate(username, password):
        result = {
            'id': 'cvrc',
            'email': 'some@example.com',
        }
        return result
