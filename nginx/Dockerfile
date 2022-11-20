FROM nginx
# COPY ./default.conf /etc/nginx/conf.d/default.conf

WORKDIR /app
COPY ./default.conf.template .

COPY ./docker-entrypoint.sh .
# EXPOSE $PORT
EXPOSE $PORT_SSL
ENTRYPOINT ["/app/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
