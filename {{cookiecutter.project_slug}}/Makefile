.PHONY: venv, tests

VENV = ./venv
BIN = $(VENV)/bin
PYTHON = $(BIN)/python

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -rf .pytest_cache
	@rm -rf htmlcov
	@rm -f .coverage
	@rm -f coverage.xml
	@rm -f *.log

venv:
	@if [ ! -d "venv" ]; then python3 -m venv venv; fi

requirements: venv
	@$(BIN)/pip3 install --upgrade pip
	@$(BIN)/pip3 install -r requirements/common.txt

local: venv
	@$(BIN)/pip3 install --upgrade pip
	@$(BIN)/pip3 install -r requirements/dev.txt

run:
	FLASK_CONFIG="default" FLASK_ENV="development" FLASK_APP="{{ cookiecutter.package_name }}:create_app('development')" $(BIN)/flask run

tests:
	@$(BIN)/py.test -x tests/

coverage:
	@$(BIN)/py.test -x --cov app/ --cov-report=xml --cov-report=term-missing tests/

check:
	@$(BIN)/flake8
	@$(BIN)/isort --check