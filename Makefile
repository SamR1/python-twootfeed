include Makefile.config
-include Makefile.custom.config
.SILENT:

clean:
	rm -fr $(VENV)

install:
	test -d $(VENV) || virtualenv $(VENV) -p $(PYTHON_VERSION)
	$(PIP) install -r $(REQUIREMENTS)

lint:
	$(PYTEST) --flake8 --isort -m "flake8 or isort" python-twootfeed

serve:
	$(FLASK) run --with-threads -h $(HOST) -p $(PORT)
