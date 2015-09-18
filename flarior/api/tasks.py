from .namespaces import ns_tasks
from flask.ext.restplus import Resource
from . import api
from .fields import task_fields


@ns_tasks.route('', endpoint='api/tasks')
class TaskListAPI(Resource):
    @api.marshal_with(task_fields)
    def get(self):
        return []
