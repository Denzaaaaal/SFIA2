FROM python:slim

RUN mkdir ./opt/service_3

COPY . /opt/service_3

WORKDIR /opt/service_3

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install request
RUN sysctl net.ipv4.conf.all.forwarding=1
RUN iptables -P FORWARD ACCEPT


CMD python3 app.py
