# syntax=docker/dockerfile:1
FROM python:3.10.2

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV lang ja_JP.UTF-8
ENV language ja_JP:ja
ENV lc_all ja_JP.UTF-8
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y vim less
RUN apt-get -y install python3
RUN apt-get install xterm -y
RUN apt-get update && apt-get install firefox-esr -y
RUN pip install matplotlib
RUN apt-get update && apt-get install python-tk -y
RUN curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list
RUN apt-get update && apt-get install elasticsearch
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -U kaleido

WORKDIR /stock_app
COPY requirements.txt /stock_app/
COPY .. /stock_app/
RUN pip install -r requirements.txt



