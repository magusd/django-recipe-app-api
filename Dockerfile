FROM python:3.9-alpine3.13 as base
LABEL maintainer="github.com/magusd"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-dev \
      build-base postgresql-dev musl-dev && \
    pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt && \
    apk del .tmp-build-dev && \
    adduser \
        --disabled-password \
        --no-create-home \
        django

USER django

FROM base as prod
COPY ./app /app

FROM prod as dev
USER root
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
RUN pip install -r /tmp/requirements.dev.txt
USER django



EXPOSE 8000
