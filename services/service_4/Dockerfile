FROM python:slim

RUN mkdir ./opt/service_4

COPY . /opt/service_4

WORKDIR /opt/service_4

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install request
RUN sysctl net.ipv4.conf.all.forwarding=1
RUN iptables -P FORWARD ACCEPT


CMD python3 app.py
