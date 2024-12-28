#!/bin/bash

set -e ${DEBUG:+-x}

# Redirect all scripts output + leaving stdout to container payload.
exec 3>&1


if [ "$1" = "nginx" ]; then
  exec nginx -c /etc/nginx/nginx.conf -e /dev/stderr
elif [ "$1" = "uwsgi" ]; then
  exec uwsgi --ini /label-studio/deploy/uwsgi.ini
elif [ "$1" = "migrate" ]; then
  exec python3 /label-studio/label_studio/manage.py locked_migrate >&3
else
  exec "$@"
fi
