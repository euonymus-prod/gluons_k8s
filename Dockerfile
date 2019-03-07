# https://hub.docker.com/_/python/
FROM python:3.6.4

RUN apt-get -q update && apt-get install -y -q \
  sqlite3 --no-install-recommends \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV LANG C.UTF-8

RUN pip install --upgrade pip

RUN python -m venv venv
ENV VIRTUAL_ENV /venv
ENV PATH /venv/bin:$PATH

RUN mkdir -p /app
WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

ADD . /app

WORKDIR /app/src
CMD gunicorn -b :8000 gluons.wsgi
