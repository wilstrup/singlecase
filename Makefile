PYTHON ?=python3

.PHONY: clean test

venv: pyproject.toml setup.py
	$(PYTHON) -m venv venv --clear --prompt sc
	./venv/bin/pip install wheel twine
	./venv/bin/python -m pip install -e .[dev]

clean:
	rm -rf venv build dist

test: venv
	./venv/bin/pytest

dist: test
	rm -rf dist
	./venv/bin/python -m build

upload-test:
	./venv/bin/twine upload --repository testpypi dist/*

upload:
	./venv/bin/twine upload dist/*