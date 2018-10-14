include Makefile.config
-include Makefile.custom.config
.SILENT:

clean:
	rm -fr $(VENV)

create-mastodon-cli:
	$(PYTHON) twootfeed/utils/create_mastodon_client.py

install:
	test -d $(VENV) || virtualenv $(VENV) -p $(PYTHON_VERSION)
	$(PIP) install -r $(REQUIREMENTS)
	test -e twootfeed/config.yml || cp twootfeed/config.example.yml twootfeed/config.yml

lint:
	$(PYTEST) --flake8 --isort -m "flake8 or isort" twootfeed

serve:
	$(FLASK) run --with-threads -h $(HOST) -p $(PORT)
