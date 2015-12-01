from flask_restplus import Resource
from . import api
from .namespaces import ns_auth
from .fields import get_auth_fields as get_fields


@ns_auth.route('', endpoint='api/auth')
class Auth(Resource):
    @api.marshal_with(get_fields)
    def get(self):
        return []
