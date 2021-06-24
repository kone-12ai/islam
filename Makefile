SHELL := /bin/bash
MANAGE := python manage.py

TEST_SETTINGS := test

.PHONY: all help deps static migrate restart update deploy

all: help

help:
	@echo "Usage:"
	@echo "  make deploy - pull and deploy the update"
	@echo "  make test - run automated tests"

pip-install:
	pip install -r requirements.txt

pipenv-install:
	pipenv install

generate-requirement:
	pipenv lock -r > requirements.txt

migratedb:
	$(MANAGE) makemigrations
	$(MANAGE) migrate

createsuperuser:
	$(MANAGE) createsuperuser --username='taleeb' --email='flavienhugs@pm.me'
	
collectstatic:
	$(MANAGE) collectstatic

dumpdata:
	$(MANAGE) dumpdata --indent=4 --format=json blog.post > __backups__/posts.json

loaddata:
	$(MANAGE) loaddata __backups__/posts.json

test-deploy:
	$(MANAGE) check --deploy

deploy:
	$(MANAGE) collectstatic
	$(MANAGE) makemigrations
	$(MANAGE) migrate
	$(MANAGE) loaddata
