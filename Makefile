build:
	docker-compose build

run:
	docker-compose up

reqs requirements:
	pip install pipenv
	pipenv install

check:
	pipenv run flake8 .
	pipenv run black . --fast --check .
	pipenv run isort --check-only .
