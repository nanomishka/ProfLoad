FROM python:2-slim

ENV APP_HOME="/app/"
WORKDIR ${APP_HOME}

RUN apt-get update
RUN apt-get install -y libmariadb-dev gcc

COPY requirements.txt .
RUN pip install -r requirements.txt
