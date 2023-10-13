REGISTRY=ghcr.io/akundev
IMAGE_NAME=akundotdev
CONTAINER_NAME=akundotdev_container
VERSION=0.1.0

lint:
	@echo "Running lint..."
	pipenv run ruff check --fix -e .
	pipenv run black .
	pipenv run djlint . --reformat

build:
	@echo "Building..."
	docker build -t $(REGISTRY)/$(IMAGE_NAME):$(VERSION) .
	docker tag $(REGISTRY)/$(IMAGE_NAME):$(VERSION) $(REGISTRY)/$(IMAGE_NAME):latest

push:
	@echo "Pushing..."
	docker push $(REGISTRY)/$(IMAGE_NAME):$(VERSION)
	docker push $(REGISTRY)/$(IMAGE_NAME):latest

run:
	@echo "Running..."
	docker run \
		-it \
		--rm \
		-p 8000:8000 \
		--name $(CONTAINER_NAME) \
		-v $(PWD):/app \
		--env-file .env \
		--entrypoint python \
		$(REGISTRY)/$(IMAGE_NAME):$(VERSION) manage.py runserver 0.0.0.0:8000
prod:
	@echo "Running..."
	docker run \
		-it \
		--rm \
		-d \
		-p 8000:8000 \
		--name $(CONTAINER_NAME) \
		--env-file .env \
		$(REGISTRY)/$(IMAGE_NAME):$(VERSION)

stop:
	@echo "Stopping..."
	docker stop $(CONTAINER_NAME)

pull:
	@echo "Pulling..."
	docker pull $(REGISTRY)/$(IMAGE_NAME):$(VERSION)

logs:
	@echo "Showing logs..."
	docker logs $(CONTAINER_NAME) -f

manage:
	@echo "Running manage.py..."
	docker exec -it $(CONTAINER_NAME) python manage.py $(cmd)

test:
	@echo "Running tests..."
	make manage cmd="test"

migrate:
	@echo "Running migrations..."
	make manage cmd="migrate"

makemigrations:
	@echo "Making migrations..."
	make manage cmd="makemigrations"

createsuperuser:
	@echo "Creating superuser..."
	make manage cmd="createsuperuser"

collectstatic:
	@echo "Collecting static files..."
	make manage cmd="collectstatic --noinput"