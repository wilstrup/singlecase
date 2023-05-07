PYTHON ?=python3

.PHONY: clean test

venv: requirements.txt
	$(PYTHON) -m venv venv --clear --prompt sc
	./venv/bin/pip install wheel
	./venv/bin/pip install -r requirements.txt

clean:
	rm -rf venv build dist

test: venv
	./venv/bin/pytest

dist: venv
	./venv/bin/python setup.py bdist_wheel
