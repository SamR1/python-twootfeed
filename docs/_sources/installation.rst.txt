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

    .. versionadded:: 0.7.0

    Since **twootfeed** is connected to the user account, feeds may display private private items.

    A token is now mandatory to start the application and access feeds (minimum length: 25 characters).

    Some examples for token generation:

    > with Python

    .. code-block:: bash

        $ python
        Python 3.10.5 (main, Jun  6 2022, 18:49:26) [GCC 12.1.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import secrets
        >>> secrets.token_urlsafe()
        'pgoeS3qOsLHxduzNY_gmn6p5vWZqSzqBgnb_VPupQ7o'
        >>>

    > with a linux command line

    .. code-block:: bash

        $ date | sha256sum | base64 | head -c 25; echo
        NWU2MzE1ZGM0MmVlZDg5NDNhN



- The files location can be changed with the following environment variables:

=========================== =============================================== ===========================================================================================
 variable                   description                                     app default value
=========================== =============================================== ===========================================================================================
 ``TWOOTFEED_CONFIG_DIR``   configuration and credentials files directory   **'~/.config/twootfeed/'**
 ``TWOOTFEED_CONFIG_FILE``  config file full path                           config dir + **'config.yml'** => with default value: **'~/.config/twootfeed/config.yml'**
 ``TWOOTFEED_LOG``          application log file                            `no default value (log printed on the console)`
 ``TWOOTFEED_SETTINGS``     application settings                            **'ProductionConfig'**
=========================== =============================================== ===========================================================================================

- Start the app

.. code-block:: bash

    $ twootfeed


Usage
~~~~~

The following RSS feeds are available:

- for Twitter search:

    - http://localhost:8080/tweets/<keywords>?token=XXX
    - http://localhost:8080/<keywords>?token=XXX  (*will be deprecated in a next version*)

- for Mastodon search:

    - keyword as a hashtag:

        - http://localhost:8080/toots/<hashtag>?token=XXX (without the leading #)

    - query:

        - http://localhost:8080/toots/search/<query>?token=XXX
        - http://localhost:8080/toot_search/<query>?token=XXX (*will be deprecated in a next version*)

- for Mastodon connected user favorites:

    - http://localhost:8080/toots/favorites?token=XXX
    - http://localhost:8080/toot_favorites?token=XXX (*will be deprecated in a next version*)

- for Mastodon connected user bookmarks:

    - http://localhost:8080/toots/bookmarks?token=XXX

- for Mastodon connected user home timeline:

    - http://localhost:8080/toots/home_timeline?token=XXX

where XXX is the token set in configuration.