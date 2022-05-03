FROM python:3.7-alpine
LABEL maintainer="Michael O'Grady"

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app


RUN adduser -D user
USER user
