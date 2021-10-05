include Makefile.config
-include Makefile.custom.config
.SILENT:

clean:
	rm -fr $(VENV)
	rm -fr *.egg-info
	rm -fr .eggs
	rm -rf .pytest_cache
	rm -fr build
	rm -rf dist

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
	$(FLASK) run --with-threads -h $(HOST) -p $(PORT)

run:
	FLASK_ENV=production && $(GUNICORN) -b 127.0.0.1:5000 "$(FLASK_APP):create_app()" --error-logfile $(GUNICORN_LOG)

venv:
	test -d $(VENV) || $(PYTHON_VERSION) -m venv $(VENV)
	$(PIP) install -U pip setuptools

test:
	$(PYTEST) $(FLASK_APP) --cov $(FLASK_APP) --cov-report term-missing $(PYTEST_ARGS)
