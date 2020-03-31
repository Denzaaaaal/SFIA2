FROM python:slim

# Setting up the environment
RUN mkdir ./opt/service_3
COPY . /opt/service_3
WORKDIR /opt/service_3
RUN apt update -y

# Installing Dependencies
RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install request

# Running the application
CMD python3 app.py
