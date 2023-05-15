FROM python:3.11.2-slim

ARG REDIS_PASSWORD 
ARG REDIS_PORT 
ARG REDIS_ADDRESS 
ARG REDIS_USER 
ARG ANSIBLE 

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN touch redis.credit && \
echo $REDIS_PASSWORD >> redis.credit && \
echo $REDIS_PORT >> redis.credit && \
echo $REDIS_ADDRESS >> redis.credit && \
echo $REDIS_USER >> redis.credit


RUN touch password.ansible && \
echo $ANSIBLE  >> password.ansible





RUN ansible-vault encrypt redis.credit --vault-password-file=password.ansible
