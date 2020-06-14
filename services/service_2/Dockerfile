FROM python:slim

# Setting up the environment
RUN mkdir ./opt/service_2
# Uncomment line 6 when not using docker_compose_local.yml
# COPY . /opt/service_2
WORKDIR /opt/service_2
RUN apt update -y

# Installing Dependencies
RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install request

# Running the application
CMD python3 app.py