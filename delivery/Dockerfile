FROM python:3.10
WORKDIR /app
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install postgresql-client -y
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
# CMD gunicorn -w 3 --chdir ./ delivery.wsgi --bind 0.0.0.0:8000
