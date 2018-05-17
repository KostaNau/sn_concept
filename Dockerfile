FROM python:alpine

ENV PYTHONUNBUFFERED 1
ENV DATABASE_SOCIAL_NETWORK_DB="psql://postgres:postgres@db:5432/sn_concept"
ENV DJANGO_SECRET_KEY="kt_^#m3=lv38okqh1$0)&d+1=_fu@69=82*8imh-^a=xk_sqet"
ENV PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

WORKDIR /sn_concept

COPY . .

RUN apk update && \
 apk add --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install --no-cache-dir -r requirements/base.txt

EXPOSE 8001
