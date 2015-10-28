#!/bin/bash

NAME=weether
DJANGO_WSGI_MODULE=weether.wsgi
LOGFILE=/home/asnelzin/weether/logs/main.log
NUM_WORKERS=3
USER=asnelzin
GROUP=asnelzin

source /home/asnelzin/.virtualenvs/weether/bin/postactivate
exec /home/asnelzin/.virtualenvs/weether/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
    --name=$NAME \
    --workers=$NUM_WORKERS \
    --user=$USER --group=$GROUP \
    --bind=localhost:8002 \
    --log-level=debug \
    --log-file=$LOGFILE
