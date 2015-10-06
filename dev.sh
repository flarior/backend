#!/bin/bash

BACKEND_ROOT=$(readlink -f $(dirname $0))
FRONTEND_ROOT=$(readlink -f "${BACKEND_ROOT}/../frontend")

tmux new-session -s "flarior" -d "${BACKEND_ROOT}/bin/start.sh"
tmux splitw -h -p 50 -t 0 -c "${FRONTEND_ROOT}" "${FRONTEND_ROOT}/bin/start.sh"
tmux a
