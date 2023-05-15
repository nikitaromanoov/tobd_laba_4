FROM python:3.11.2-slim



ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN touch redis.credit && echo $REDIS_PASSWORD >> redis.credit && echo $REDIS_PORT >> redis.credit && echo $REDIS_ADDRESS >> redis.credit && echo $REDIS_USER >> redis.credit

RUN touch password.ansible && echo $ANSIBLE >> password.ansible

RUN cat redis.credit
RUN cat password.ansible

RUN ansible-vault encrypt redis.credit --vault-password-file=password.ansible
