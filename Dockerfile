FROM python:3.8-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN touch password.ansible $$ echo $ANSIMBLE >> password.ansible
