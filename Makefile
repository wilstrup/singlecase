PYTHON ?=python3

.PHONY: clean test

venv:
	$(PYTHON) -m venv venv --clear --prompt sc
	./venv/bin/pip install wheel
	./venv/bin/python -m pip install -e .[dev]

clean:
	rm -rf venv build dist

test: venv
	./venv/bin/pytest

dist: venv
	./venv/bin/python setup.py bdist_wheel
