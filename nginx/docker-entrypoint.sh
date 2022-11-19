#!/usr/bin/env sh
set -eu

envsubst '\$DOMAIN \$COMPOSE_PROJECT_NAME \$PORT \$PORT_SSL' < /app/default.conf.template > /etc/nginx/conf.d/default.conf

exec "$@"