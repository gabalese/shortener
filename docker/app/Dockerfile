FROM ubuntu:14.04
MAINTAINER Gabriele Alese <gabriele@alese.it>

ENV DEBIAN_FRONTEND noninteractive

ADD . /www
RUN apt-get update
RUN apt-get install -y openjdk-7-jre
RUN apt-get install -y postgresql python-dev python-pip python-psycopg2 curl tmux supervisor
RUN curl -o /opt/logstash-1.4.2.tar.gz https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz
RUN tar zxvf /opt/logstash-1.4.2.tar.gz
ADD docker/app/files/ /etc/files
ADD docker/app/files/supervisord.conf /etc/supervisor/conf.d/logstash.conf

RUN pip install -r /www/requirements.txt

RUN touch /var/log/uwsgi.log
RUN mkdir -p mkdir /var/run/uwsgi
RUN touch /var/run/uwsgi/uwsgi.pid

EXPOSE 8000

CMD bash -c 'supervisord -n'
