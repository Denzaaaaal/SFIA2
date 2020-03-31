FROM python:slim

# Setting up the environment
RUN mkdir ./opt/service_1
COPY . /opt/service_1
WORKDIR /opt/service_1
RUN apt update -y

# Installing dependencies
RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install request

# Running the application
CMD python3 app.py
