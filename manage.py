#!/usr/bin/env python
import os
from datetime import datetime

from flask import Flask
from flask.ext.script import Manager, Server
from flask.ext.security.script import CreateUserCommand

from flarior import Flarior
from config import configs


config_name = os.getenv('FLASK_CONFIG') or 'default'
app = Flask(__name__)
app.config.from_object(configs[config_name])
flarior = Flarior(app)
manager = Manager(app)
manager.add_command(
    "runserver",
    Server(
        host="0.0.0.0",
        use_reloader=True,
        use_debugger=True
    )
)
manager.add_command('create_user', CreateUserCommand)


from flarior.models import Role, User, UserRoles
@manager.command
def syncdb():
    for Model in (Role, User, UserRoles):
        Model.create_table(fail_silently=True)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    current_time = datetime.now()
    livereload_path = os.path.abspath('../frontend/app/livereload.txt')
    with open(livereload_path, 'w+') as livereload:
        livereload.write(str(current_time))
    manager.run()
