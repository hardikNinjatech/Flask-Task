.PHONY: run migrate test

run:
	python run.py

migrate:
	flask db migrate -m "Initial migration"
	flask db upgrade

test:
	pytest