from flask.ext.restplus import apidoc
from flask.ext.security import Security, PeeweeUserDatastore
from flask.ext.security.utils import verify_password
from flask_jwt import JWT
from flask_peewee.db import Database


current_app = None


class Flarior(object):
    """
    Flarior app
    """

    jwt = JWT()
    db = None
    security = Security()
    user_datastore = None

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

        self.db = Database(self.app)
        from models import Role, User, UserRoles
        self.user_datastore = PeeweeUserDatastore(
            self.db,
            User,
            Role,
            UserRoles
        )
        self.security.init_app(self.app, self.user_datastore)
        self.jwt.init_app(app)

    @jwt.authentication_handler
    def authenticate(username, password):
        from models import User
        try:
            user = User.get(email=username)
        except User.DoesNotExist:
            return None
        if verify_password(password, user.password):
            return user

    @jwt.user_handler
    def load_user(payload):
        from models import User
        try:
            user = User.get(id=payload['user_id'])
        except User.DoesNotExist:
            return None
        return user
