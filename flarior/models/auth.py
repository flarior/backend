from flask.ext.security import (
    UserMixin,
    RoleMixin
)
from peewee import (
    CharField,
    TextField,
    BooleanField,
    DateTimeField,
    ForeignKeyField,
    Model,
)
from .. import current_app

db = current_app.db


class Role(db.Model, RoleMixin):
    name = CharField(unique=True)
    description = TextField(null=True)


class User(db.Model, UserMixin):
    email = TextField()
    password = TextField()
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(null=True)


class UserRoles(db.Model):
    user = ForeignKeyField(User, related_name='roles')
    role = ForeignKeyField(Role, related_name='users')
    name = property(lambda self: self.role.name)
    description = property(lambda self: self.role.description)
