
.PHONY: install install-requirements

install:
	python setup.py develop

install-requirements: requirements.txt
	python -m pip install -r requirements.txt

