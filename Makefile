# Name of the project
PROJ = wuutils
SRC_DIR = $(PROJ)

# Directory to place the python virtual environment
VENV_DIR = ~/venv/$(PROJ)

# Install Requirements via PIP
init:
	pip install -r requirements.txt

# Code checks
lint:
	pylint --disable=R,C $(SRC_DIR)/*.py
	pylint --disable=R,C examples/*.py

flake:
	flake8 .

test: flake lint

# Clean up
clean-pyc:
	find ./$(SRC_DIR) -name '*.pyc' -print -delete
	find ./$(SRC_DIR) -name '*.pyo' -print -delete

clean-build:
	python setup.py clean
	rm -rvf build/
	rm -rvf dist/
	rm -rvf *.egg-info

clean: clean-build clean-pyc

# Make the Virtual Environment
virtualenv:
	python3 -m venv $(VENV_DIR)
		
	@echo "You may now execute: source $(VENV_DIR)/bin/activate"
