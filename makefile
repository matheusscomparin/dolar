.PHONY: run

include .env
export

run:
	docker-compose up --build