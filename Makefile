include Makefile.config
-include Makefile.custom.config
.SILENT:

clean:
	rm -fr $(VENV)

create-mastodon-cli:
	$(PYTHON) python-twootfeed/create_mastodon_client.py

install:
	test -d $(VENV) || virtualenv $(VENV) -p $(PYTHON_VERSION)
	$(PIP) install -r $(REQUIREMENTS)
	cp python-twootfeed/config.example.yml python-twootfeed/config.yml

lint:
	$(PYTEST) --flake8 --isort -m "flake8 or isort" python-twootfeed

serve:
	$(FLASK) run --with-threads -h $(HOST) -p $(PORT)
