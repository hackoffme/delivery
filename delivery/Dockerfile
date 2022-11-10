FROM python:3.10
WORKDIR /usr/src/app
RUN apt-get update -y
RUN apt-get upgrade -y
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get install postgresql-client -y
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . .

COPY ./entrypoint.sh /usr/local/bin/
COPY ./wait-for-postgres.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/wait-for-postgres.sh
# # run entrypoint.sh
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]