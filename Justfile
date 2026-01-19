lint:
	poetry run ruff check . --fix
	poetry run ruff format .
	poetry run mypy .
	poetry run bandit -r spongebobify --severity-level high

test:
	poetry run pytest

check: lint test
