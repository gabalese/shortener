build: build_app build_elasticsearch

build_elasticsearch:
	cp docker/elasticsearch/Dockerfile .
	docker build -t shortener-elasticsearch .
	rm Dockerfile

build_app:
	cp docker/app/Dockerfile .
	docker build -t shortener-app .
	rm Dockerfile

run:
	docker run -v .:/www/ --link shortener-elasticsearch:es -p 80:80 shortener-app
