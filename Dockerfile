FROM python:3.9-alpine3.13 as prod
LABEL maintainer="github.com/magusd"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    adduser \
        --disabled-password \
        --no-create-home \
        django

USER django

FROM prod as dev
USER root
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
RUN pip install -r /tmp/requirements.dev.txt
USER django



EXPOSE 8000
