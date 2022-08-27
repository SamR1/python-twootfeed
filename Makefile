include Makefile.config
-include Makefile.custom.config
.SILENT:

check: type-check lint test

clean:
	rm -rf .mypy_cache
	rm -rf .pytest_cache

clean-all: clean
	rm -fr $(VENV)
	rm -fr *.egg-info
	rm -fr .eggs
	rm -fr build
	rm -rf dist
	rm -rf *.log

create-mastodon-cli:
	$(PYTHON) $(FLASK_APP)/utils/create_mastodon_client.py

html:
	rm -rf docsrc/build
	rm -rf docs/*
	touch docs/.nojekyll
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	cp -a docsrc/build/html/. docs

install: venv
	$(PIP) install -e .[test,doc]
	test -e $(FLASK_APP)/config.yml || cp $(FLASK_APP)/config.example.yml $(FLASK_APP)/config.yml

lint:
	$(PYTEST) --flake8 --isort --black -m "flake8 or isort or black" $(FLASK_APP)

lint-fix:
	$(BLACK) $(FLASK_APP)

serve:
	echo 'Running on http://$(HOST):$(PORT)'
	$(FLASK) run --with-threads -h $(HOST) -p $(PORT)

run:
	echo 'Running on http://localhost:$(PORT)'
	FLASK_ENV=production && $(GUNICORN) -b 127.0.0.1:$(PORT) "$(FLASK_APP):create_app()" --error-logfile $(GUNICORN_LOG)

venv:
	test -d $(VENV) || $(PYTHON_VERSION) -m venv $(VENV)
	$(PIP) install -U pip setuptools

test:
	$(PYTEST) $(FLASK_APP) --cov $(FLASK_APP) --cov-report term-missing $(PYTEST_ARGS)

type-check:
	echo 'Running mypy...'
	$(MYPY) $(FLASK_APP)
