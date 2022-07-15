Installation and usage
######################

Requirements
~~~~~~~~~~~~

- Python 3.7+
- API keys Twitter and/or Mastodon


Installation
~~~~~~~~~~~~

- Install from pip

.. code-block:: bash

    $ pip install twootfeed


- Initialize the configuration file

.. code-block:: bash

    $ twootfeed_init


- Fill in fields for the client(s) you will use in **'~/.config/twootfeed/config.yml'** :

    - for **Twitter** : see https://apps.twitter.com

    copy/paste the Twitter API key values in **config.yml** file ('*consumerKey*' and '*consumerSecret*')

    - for **Mastodon** : see `Python wrapper for the Mastodon API <https://mastodonpy.readthedocs.io/>`_

    use the included script which will register your app and prompt you to log in, creating the credential files for you.

    .. code-block:: bash

        $ twootfeed_create_mastodon_cli

    Update the `feed and app parameters <parameters.html>`_.


- The files location can be changed with the following environment variables:

========================= =============================================== ===========================================================================================
 variable                 description                                     app default value
========================= =============================================== ===========================================================================================
 `TWOOTFEED_CONFIG_DIR`   configuration and credentials files directory   **'~/.config/twootfeed/'**
 `TWOOTFEED_CONFIG_FILE`  config file full path                           config dir + **'config.yml'** => with default value: **'~/.config/twootfeed/config.yml'**
 `TWOOTFEED_LOG`          application log file                            _no default value (log printed on the console)_
========================= =============================================== ===========================================================================================

- Start the app

.. code-block:: bash

    $ twootfeed


Usage
~~~~~

The RSS feeds are available on these urls:

- for Twitter search:

    - http://localhost:8080/tweets/<keywords>
    - http://localhost:8080/<keywords>  (*will be deprecated in a next version*)

- for Mastodon search:

    - keyword as a hashtag:

        - http://localhost:8080/toots/<hashtag> (without the leading #)

    - query:

        - http://localhost:8080/toots/search/<query>
        - http://localhost:8080/toot_search/<query> (*will be deprecated in a next version*)

- for Mastodon connected user favorites:

    - http://localhost:8080/toots/favorites
    - http://localhost:8080/toot_favorites (*will be deprecated in a next version*)

- for Mastodon connected user bookmarks:

    - http://localhost:8080/toots/bookmarks

- for Mastodon connected user home timeline:

    - http://localhost:8080/toots/home_timeline