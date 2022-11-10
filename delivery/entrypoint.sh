#!/bin/sh

NAME="gunicorn"
DIR=/usr/src/app
WORKERS=3
BIND=0.0.0.0:8000
DJANGO_SETTINGS_MODULE=delivery.settings
LOG_LEVEL=info
LOG_FILE=/var/log/gunicorn/log.log
LOG_ERR=/var/log/gunicorn/error.log
LOG_ACCESS=/var/log/gunicorn/access.log
mkdir /var/log/gunicorn
touch $LOG_FILE
touch $LOG_ERR
touch $LOG_ACCESS

cd $DIR

# export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
# exec gunicorn -w 3 --chdir ./ delivery.wsgi --bind 0.0.0.0:8000



exec gunicorn delivery.wsgi:application \
  --name $NAME \
  --workers $WORKERS \
  --bind=$BIND \
  --log-level=$LOG_LEVEL \
  --log-file=$LOG_FILE \
  --error-logfile=$LOG_ERR \
  --access-logfile=$LOG_ACCESS \
  --chdir ./ \
  --capture-output 
