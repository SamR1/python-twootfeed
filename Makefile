include Makefile.config
-include Makefile.custom.config
.SILENT:

clean:
	rm -fr $(VENV)
	rm -fr *.egg-info

create-mastodon-cli:
	$(PYTHON) twootfeed/utils/create_mastodon_client.py

install:
	test -d $(VENV) || virtualenv $(VENV) -p $(PYTHON_VERSION)
	$(PIP) install -e .[test]
	test -e twootfeed/config.yml || cp twootfeed/config.example.yml twootfeed/config.yml

serve:
	$(FLASK) run --with-threads -h $(HOST) -p $(PORT)

run:
	FLASK_ENV=production && $(GUNICORN) -b 127.0.0.1:5000 "twootfeed:create_app()" --error-logfile $(GUNICORN_LOG)

test:
	$(PYTHON) setup.py test
