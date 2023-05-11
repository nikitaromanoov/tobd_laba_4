FROM python:3.8-slim

RUN apk update

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app
