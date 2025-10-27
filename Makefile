REGISTRY=ghcr.io/akundev
IMAGE_NAME=akundotdev
CONTAINER_NAME=akundotdev_container
VERSION=0.1.0

ENV=pipenv run
CMD=python

k=.

lint:
	${ENV} ruff check --fix -e .
	${ENV} black .
	${ENV} djlint ./templates/ --reformat

runserver:
	${ENV} $(CMD) manage.py runserver

makemigrations:
	${ENV} $(CMD) manage.py makemigrations

collectstatic:
	${ENV} $(CMD) manage.py collectstatic

migrate:
	${ENV} $(CMD) manage.py migrate

accounts_demo:
	${ENV} $(CMD) manage.py accounts_demo

medtis_demo:
	${ENV} $(CMD) manage.py medtis_demo

test:
	pipenv run python manage.py test -k=$(k)

cov:
	${ENV} coverage run --source='.' manage.py test
	${ENV} coverage report
	${ENV} coverage html

build:
	docker build -t $(REGISTRY)/$(IMAGE_NAME):$(VERSION) .
	docker tag $(REGISTRY)/$(IMAGE_NAME):$(VERSION) $(REGISTRY)/$(IMAGE_NAME):latest

push:
	docker push $(REGISTRY)/$(IMAGE_NAME):$(VERSION)
	docker push $(REGISTRY)/$(IMAGE_NAME):latest

prod:
	docker run \
		-it \
		--rm \
		-d \
		-p 8000:8000 \
		--name $(CONTAINER_NAME) \
		--env-file .env \
		$(REGISTRY)/$(IMAGE_NAME):$(VERSION)

stop:
	docker stop $(CONTAINER_NAME)

restart:
	docker restart $(CONTAINER_NAME)

pull:
	docker pull $(REGISTRY)/$(IMAGE_NAME):latest

logs:
	docker logs $(CONTAINER_NAME) -f


dc-up:
	docker compose up --build

dc-down:
	docker compose down -v

