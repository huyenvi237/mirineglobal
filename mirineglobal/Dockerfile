# syntax=docker/dockerfile:1
FROM python:3.10.2

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

WORKDIR /stock_app
COPY requirements.txt /stock_app/
COPY .. /stock_app/
RUN pip install -r requirements.txt
