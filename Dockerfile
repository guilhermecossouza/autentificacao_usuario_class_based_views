FROM python:3.8

MAINTAINER Guilherme Costa

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /autenticacao
WORKDIR /autenticacao
COPY ./autenticacao /autenticacao