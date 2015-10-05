#!/usr/bin/env fish

tmux new-session -s "flarior" -d "/vagrant/backend/manage.py runserver"
tmux splitw -h -p 50 -t 0 -c /vagrant/frontend "/vagrant/frontend/node_modules/gulp/bin/gulp.js"
tmux a
