FROM python:3.8-slim

RUN apk update

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app


RUN  apk curl && curl -fsSL https://packages.redis.io/gpg | gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg  && echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list && apt-get update && apt-get install redis &&pip install -r requirements.txt
