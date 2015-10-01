from .namespaces import ns_tasks
from . import api
from .fields import task_fields
from resources import ProtectedResource


@ns_tasks.route('', endpoint='api/tasks')
class TaskListAPI(ProtectedResource):
    @api.marshal_with(task_fields)
    def get(self):
        return []
