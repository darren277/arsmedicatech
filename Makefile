include .env

# To initialize `.venv`: `python3 -m venv .venv`.

run-flask:
	.\.venv\Scripts\activate
	set FLASK_APP=.\app.py
	flask run --host=$(HOST) --port=$(PORT)

# Or, if that doesn't work: python app.py --host=0.0.0.0 --port=3123

# TODO: Doesn't work for some reason. Currently have to run each command manually.
run-flask-linux:
	. .venv/bin/activate
	export FLASK_APP=./app.py
	flask run --host=$(HOST) --port=$(PORT)


run-react-dev:
	API_URL=$(API_URL) npm start


run-react-prod:
	npm install
	API_URL=$(API_URL) npm run build
	npx http-server ./dist -p $(REACT_PORT)


run-mcp:
	.\.venv\Scripts\activate
	python lib/llm/mcp/mcp_server.py


local-encryption-key:
	@echo "Generating encryption key..."
	@python3 -c "import secrets, string; print('ENCRYPTION_KEY=' + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32)))"



# Docker
auth:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $(DOCKER_REGISTRY)

create-repos:
	aws ecr create-repository --repository-name $(FLASK_IMAGE) --region us-east-1 || true
	aws ecr create-repository --repository-name $(REACT_IMAGE) --region us-east-1 || true
	aws ecr create-repository --repository-name $(MCP_SERVER_IMAGE) --region us-east-1 || true

docker-mcp:
	docker build --build-arg PORT=$(MCP_SERVER_PORT) -t $(DOCKER_REGISTRY)/$(MCP_SERVER_IMAGE):$(MCP_SERVER_VERSION) -f Dockerfile.mcp .
	docker push $(DOCKER_REGISTRY)/$(MCP_SERVER_IMAGE):$(MCP_SERVER_VERSION)
	kubectl rollout restart deployment $(MCP_SERVER_DEPLOYMENT) --namespace=$(NAMESPACE)

docker-flask:
	docker build --build-arg PORT=$(FLASK_PORT) -t $(DOCKER_REGISTRY)/$(FLASK_IMAGE):$(FLASK_VERSION) -f Dockerfile.flask .
	docker push $(DOCKER_REGISTRY)/$(FLASK_IMAGE):$(FLASK_VERSION)
	kubectl rollout restart deployment $(FLASK_DEPLOYMENT) --namespace=$(NAMESPACE)

docker-react:
	docker build --build-arg PORT=$(REACT_PORT) --build-arg API_URL=$(API_URL) -t $(DOCKER_REGISTRY)/$(REACT_IMAGE):$(REACT_VERSION) -f Dockerfile.react .
	docker push $(DOCKER_REGISTRY)/$(REACT_IMAGE):$(REACT_VERSION)
	kubectl rollout restart deployment $(REACT_DEPLOYMENT) --namespace=$(NAMESPACE)


# Kubernetes and Helm
k8s-init:
	kubectl create namespace $(NAMESPACE)

k8s-auth:
	kubectl create secret docker-registry ecr-secret --docker-server=$(DOCKER_REGISTRY) --docker-username=AWS --docker-password=$(DOCKER_PASSWORD) --namespace=$(NAMESPACE)

k8s-encryption-key:
	@echo "Generating encryption key..."
	@python3 -c "import secrets, string; print('ENCRYPTION_KEY=' + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(32)))"
	kubectl create secret generic encryption-key --from-literal=ENCRYPTION_KEY=your_generated_key_here --namespace=$(NAMESPACE) || true

SECRETS=--set surrealdb.secret.user=$(SURREALDB_USER) --set surrealdb.secret.pass=$(SURREALDB_PASS) --set migration-openai.apiKey=$(MIGRATION_OPENAI_API_KEY)

k8s-create-secrets:
	kubectl create secret generic surreal-secret --from-literal=user=$(SURREALDB_USER) --from-literal=pass=$(SURREALDB_PASS) --namespace=$(NAMESPACE) || true
	kubectl create secret generic migration-openai-secret --from-literal=apiKey=$(MIGRATION_OPENAI_API_KEY) --namespace=$(NAMESPACE) || true

k8s-deploy: k8s-create-secrets
	kubectl create namespace $(NAMESPACE) || true
	helm upgrade --install $(NAMESPACE) ./k8s --namespace $(NAMESPACE) $(SECRETS) -f ./k8s/values.yaml

k8s-debug:
	kubectl create namespace $(NAMESPACE) --dry-run=client -o yaml | kubectl apply -f -
	helm template $(NAMESPACE) ./k8s -f ./k8s/values.yaml | kubectl apply --namespace $(NAMESPACE) -f - --dry-run=server


# Tests
test-crud:
	python test_api.py

test-schema:
	python test_schema.py

test-surrealdb:
	python test_db.py

test-create-and-retrieve:
	python test_create_and_retrieve.py

# Playwright E2E Tests
test-e2e:
	npm run test:e2e

test-e2e-ui:
	npm run test:e2e:ui

test-e2e-headed:
	npm run test:e2e:headed

test-e2e-debug:
	npm run test:e2e:debug

test-e2e-report:
	npm run test:e2e:report

test-e2e-install:
	npm run test:e2e:install


# S3

# Create S3 bucket for PDFs...
s3-create:
	aws s3api create-bucket --profile $(AWS_PROFILE) --region $(AWS_REGION) --bucket $(S3_BUCKET) | true
	aws s3api put-public-access-block --profile $(AWS_PROFILE) --region $(AWS_REGION) --bucket $(S3_BUCKET) --public-access-block-configuration BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true | true
	aws s3api put-bucket-policy --profile $(AWS_PROFILE) --region $(AWS_REGION) --bucket $(S3_BUCKET) --policy file://config/s3_iam_bucket_policy.json | true


s3-iam:
	aws iam create-user --profile $(AWS_PROFILE) --region $(AWS_REGION) --user-name flask-s3-writer | true
	aws iam put-user-policy --profile $(AWS_PROFILE) --region $(AWS_REGION) --user-name flask-s3-writer --policy-name FlaskS3WritePolicy --policy-document file://config/flask_s3_write_policy.json | true
	aws iam create-access-key --user-name flask-s3-writer

textract-iam:
	aws iam create-user --profile $(AWS_PROFILE) --region $(AWS_REGION) --user-name flask-textract-user | true
	aws iam put-user-policy --profile $(AWS_PROFILE) --region $(AWS_REGION) --user-name flask-textract-user --policy-name TextractReadPolicy --policy-document file://config/textract_read_write_policy.json | true
	aws iam create-access-key --user-name flask-textract-user


# Celery
CELERY_IMAGE=celery-worker
CELERY_VERSION=1.0.0


celery-docker:
	docker build -t $(CELERY_IMAGE):$(CELERY_VERSION) -f Dockerfile.celery .

celery-run:
	docker run -d --name celery-worker -e CELERY_BROKER_URL=redis://$(REDIS_HOST):$(REDIS_PORT)/1 -e SENTRY_DSN=$(SENTRY_DSN) -e CELERY_RESULT_BACKEND=redis://$(REDIS_HOST):$(REDIS_PORT)/1 $(CELERY_IMAGE):$(CELERY_VERSION)
