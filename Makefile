.PHONY: help
help:
	@echo '                                                                          '
	@echo 'Makefile for zookeeper demo                                                '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make help                           show help                          '
	@echo '                                                                          '
	@echo '   make up                             启动服务                            '
	@echo '   make down                           停止服务                            '
	@echo '   make logs                           查看日志                            '
	@echo '                                                                          '
	@echo '   make build                          build docker image                 '
	@echo '   make push                           push docker image                  '
	@echo '                                                                          '
	@echo '                                                                          '


t := $(shell date +'%Y-%m-%d-%H-%M-%S')

tag_name:="zookeeper-demo:$(t)"
tag_name_latest:="zookeeper-demo:latest"


.PHONY: build-push-image
build-push-image:

	docker build . -t $(tag_name)
	docker build . -t $(tag_name_latest)
	docker push  $(tag_name)
	docker push  $(tag_name_latest)

.PHONY: up
up:
	docker-compose  up -d


.PHONY: down
down:
	docker-compose  down


.PHONY: logs
logs:
	docker-compose  logs -f


.PHONY: test
test:
	curl http://localhost:9002