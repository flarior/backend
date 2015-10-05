from .namespaces import ns_tasks
from . import api
from .fields import task_fields, get_task_fields
from resources import ProtectedResource
from taskw import TaskWarriorShellout as TaskWarrior

parser = api.parser()
parser.add_argument('description', type=str, required=True, location='json')


@ns_tasks.route('', endpoint='api/tasks')
class TaskListAPI(ProtectedResource):
    @api.marshal_with(get_task_fields)
    def get(self):
        tasks = TaskWarrior(marshal=True).load_tasks()['pending']
        return tasks

    @api.expect(task_fields)
    @api.marshal_with(get_task_fields)
    def post(self):
        args = parser.parse_args()
        task = TaskWarrior(marshal=True).task_add(
            description=args.get('description')
        )
        return task
