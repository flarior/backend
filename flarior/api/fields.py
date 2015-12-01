from flask_restplus import fields
from . import api


get_auth_fields = api.model(
    'Auth', {
        'email': fields.String(required=True),
    }
)
