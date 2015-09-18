from flask.ext.restplus import fields
from . import api


task_fields = api.model(
    'Tasks', {
        'id': fields.String,
    }
)
