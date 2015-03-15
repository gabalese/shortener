FROM ubuntu:14.04

MAINTAINER Gabriele Alese <gabriele@alese.it>

RUN apt-get update
RUN apt-get install -y openjdk-7-jre
RUN apt-get install -y tmux supervisor curl

RUN curl -o /tmp/elasticsearch.tar.gz https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.2.tar.gz
RUN tar zxvf /tmp/elasticsearch.tar.gz

ADD docker/elasticsearch/files/elasticsearch.yml /elasticsearch-1.4.2/config/elasticsearch.yml
ADD docker/elasticsearch/files/supervisord.conf /etc/supervisor/conf.d/elasticsearch.conf

CMD ["supervisord -n"]
EXPOSE 9200

