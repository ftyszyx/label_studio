#!/bin/bash

set -e ${DEBUG:+-x}

# Redirect all scripts output + leaving stdout to container payload.
exec 3>&1


if [ "$1" = "nginx" ]; then
  exec nginx -c $OPT_DIR/nginx/nginx.conf -e /dev/stderr
elif [ "$1" = "label-studio-uwsgi" ]; then
  exec uwsgi --ini /label-studio/deploy/uwsgi.ini
elif [ "$1" = "label-studio-migrate" ]; then
  exec python3 /label-studio/label_studio/manage.py locked_migrate >&3
else
  exec "$@"
fi
