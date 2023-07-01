PYTHON ?=python3

.PHONY: clean test

venv:
	$(PYTHON) -m venv venv --clear --prompt sc
	./venv/bin/pip install wheel twine
	./venv/bin/python -m pip install -e .[dev]

clean:
	rm -rf venv build dist

test: venv
	./venv/bin/pytest

dist: test
	./venv/bin/python -m build

upload:
	./venv/bin/twine upload dist/*