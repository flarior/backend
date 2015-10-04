from flask.ext.restplus import fields
from . import api


task_fields = api.model(
    'Task', {
        'description': fields.String,
    }
)

get_task_fields = api.extend(
    'Get Tasks',
    task_fields,
    {
        'id': fields.Integer,
        'project': fields.String,
        'status': fields.String,
        'urgency': fields.String,
        'uuid': fields.String,
    }
)

auth_fields = api.model(
    'Auth', {
        'email': fields.String(
            description='The email',
            required=True,
            default='admin@example.com'
        ),
        'password': fields.String(
            description='The password',
            required=True,
            default='Sekrit'
        ),
    }
)

token_response = api.model(
    'Token', {
        'token': fields.String,
    }
)
