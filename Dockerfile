FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install python3-pip -y

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

RUN mkdir /employee-management
WORKDIR /employee-management
COPY ./employee-management /employee-management

