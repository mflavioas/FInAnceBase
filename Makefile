.PHONY: setup up down seed test docs ai-eval backup restore deploy-dev deploy-prod

setup:
	@echo "Setting up FinKnowledge Antigravity..."
	cp .env.example .env
	pip install -r apps/api/requirements.txt
	@echo "Setup complete."

up:
	@echo "Starting local environment..."
	docker compose -f infra/docker-compose.yml up -d

down:
	@echo "Stopping local environment..."
	docker compose -f infra/docker-compose.yml down

seed:
	@echo "Running database seeds..."
	# python db/seeds/run.py

migrate:
	@echo "Running database migrations..."
	# alembic upgrade head

test:
	@echo "Running tests..."
	pytest tests/

docs:
	@echo "Generating documentation..."
	# mkdocs build

ai-eval:
	@echo "Running AI evaluation..."
	pytest tests/ai-evals/

backup:
	@echo "Running backup..."
	# TODO: Implement backup script

restore:
	@echo "Running restore..."
	# TODO: Implement restore script

deploy-dev:
	@echo "Deploying to DEV..."
	# helm upgrade --install finknowledge-dev infra/helm/finknowledge -f infra/values-dev.yaml

deploy-prod:
	@echo "Deploying to PROD..."
	# helm upgrade --install finknowledge-prod infra/helm/finknowledge -f infra/values-prod.yaml
