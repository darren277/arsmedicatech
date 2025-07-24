include .env

docker-create:
	aws ecr create-repository --repository-name $(OSCAR_EMR_IMAGE) --region us-east-1 || true
	aws ecr create-repository --repository-name $(MARIADB_IMAGE) --region us-east-1 || true
	aws ecr create-repository --repository-name $(MIGRATIONS_IMAGE) --region us-east-1 || true


auth:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $(DOCKER_REGISTRY)


oscar-docker:
	docker build -t $(DOCKER_REGISTRY)/$(OSCAR_EMR_IMAGE):$(OSCAR_EMR_VERSION) -f ./Dockerfile .
	docker push $(DOCKER_REGISTRY)/$(OSCAR_EMR_IMAGE):$(OSCAR_EMR_VERSION)
	kubectl rollout restart deployment $(OSCAR_EMR_DEPLOYMENT) --namespace=$(NAMESPACE)

mariadb-docker:
	docker build -t $(DOCKER_REGISTRY)/$(MARIADB_IMAGE):$(MARIADB_VERSION) -f ./Dockerfile.db .
	docker push $(DOCKER_REGISTRY)/$(MARIADB_IMAGE):$(MARIADB_VERSION)
	kubectl rollout restart deployment $(MARIADB_DEPLOYMENT) --namespace=$(NAMESPACE)

migrations-docker:
	docker build -t $(DOCKER_REGISTRY)/$(MIGRATIONS_IMAGE):$(MIGRATIONS_VERSION) -f ./migrations/Dockerfile ./migrations
	docker push $(DOCKER_REGISTRY)/$(MIGRATIONS_IMAGE):$(MIGRATIONS_VERSION)
	kubectl rollout restart deployment $(MIGRATIONS_DEPLOYMENT) --namespace=$(NAMESPACE)


k8s-auth:
	kubectl create secret docker-registry ecr-secret --docker-server=$(DOCKER_REGISTRY) --docker-username=AWS --docker-password=$(DOCKER_PASSWORD) --namespace=$(NAMESPACE)
