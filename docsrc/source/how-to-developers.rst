Quick start for developers
##########################

Dependencies
~~~~~~~~~~~~

- `Flask  <http://flask.pocoo.org/>`_
- `Feedgenerator  <https://pypi.python.org/pypi/feedgenerator)>`_
- `Tweepy  <https://github.com/tweepy/tweepy>`_ (only tested with the `Twitter Standard API <https://developer.twitter.com/en/docs/tweets/search/overview/standard.html>`_)
- `Mastodon.py  <https://github.com/halcy/Mastodon.py>`_
- `pytz  <https://pypi.python.org/pypi/pytz/>`_
- `pyYAML  <https://github.com/yaml/pyyaml>`_
- `BeautifulSoup  <https://pypi.python.org/pypi/beautifulsoup4>`_
- `gunicorn  <https://gunicorn.org/>`_


Installation
~~~~~~~~~~~~

- Clone this repo :

.. code-block:: bash

    $ git clone https://github.com/SamR1/python-twootfeed.git


- Install Python virtualenv and packages

.. code-block:: bash

    $ cd python-twootfeed
    $ make install


- Fill in fields for the client(s) you will use in **python-twootfeed/config.yml** (see next step for API keys).

- Get API Keys (see `installation <installation.html#installation>`_)

- Generate token to access feed (see `installation <installation.html#installation>`_)

- Start the server

.. code-block:: bash

    $ make serve


Tests
~~~~~

.. code-block:: bash

    $ make test
