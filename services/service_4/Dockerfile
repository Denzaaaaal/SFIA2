FROM python:slim

# Setting up the environment
RUN mkdir ./opt/service_4
COPY . /opt/service_4
WORKDIR /opt/service_4
RUN apt update -y

# Installing the dependencies
RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install request

# Running the application
CMD python3 app.py
