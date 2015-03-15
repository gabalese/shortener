FROM ubuntu:14.04
MAINTAINER Gabriele Alese <gabriele@alese.it>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y openjdk-7-jre
RUN apt-get install -y postgresql python-dev python-pip python-psycopg2 curl tmux
RUN curl -o /opt/logstash-1.4.2.tar.gz https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz
RUN tar zxvf /opt/logstash-1.4.2.tar.gz
ADD files/ /tmp/files
RUN chmod +x /tmp/files/*.sh
RUN ln -s /tmp/files/logstash.conf /etc/logstash.conf
RUN ln -s /tmp/files/supervisord.conf /etc/supervisord.conf
RUN pip install -U supervisor
RUN supervisord -c /etc/supervisord.conf

EXPOSE 8000

CMD ["/tmp/files/run.sh"]
