From nginx:latest
WORKDIR /etc/nginx
RUN apt update -y
RUN apt install openssl -y
RUN rm ./conf.d/default.conf
COPY ./reverse_proxy.conf ./conf.d/.
RUN openssl req -x509 -newkey rsa:4096 -keyout cert.key -out cert.crt -days 365 -subj '/CN=localhost' -nodes