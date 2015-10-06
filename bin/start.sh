#!/bin/bash

export BACKEND_ROOT=$(readlink -f "$(dirname $0)/..")

while true; do
    vex flarior "${BACKEND_ROOT}/manage.py" runserver
    sleep 3
done
