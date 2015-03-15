build: build_app build_elasticsearch
	echo "Build all"

build_elasticsearch:
	echo "Build elasticsearch"

build_app:
	docker build -t shortener-app docker/app/
