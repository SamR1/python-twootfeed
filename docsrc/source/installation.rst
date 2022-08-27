Installation and usage
######################

Requirements
~~~~~~~~~~~~

- Python 3.7+
- API keys Twitter and/or Mastodon


Installation
~~~~~~~~~~~~

- Create and activate a virtualenv

.. code-block:: bash

    $ python -m venv .venv
    $ source .venv/bin/activate

- Install from pip

.. code-block:: bash

    (.venv) $ pip install twootfeed


- Initialize the configuration file

.. code-block:: bash

    (.venv) $ twootfeed_init


- Fill in fields for the client(s) you want to use in **'~/.config/twootfeed/config.yml'** :

    .. note::
      | Details on `feed and app parameters <parameters.html>`_.

    - for **Twitter**: see https://apps.twitter.com

    copy/paste the Twitter API key values in **config.yml** file ('*consumerKey*' and '*consumerSecret*')

    - for **Mastodon**: see `Python wrapper for the Mastodon API <https://mastodonpy.readthedocs.io/>`_

    use the included script which will register your app and prompt you to log in, creating the credential files for you.

    .. code-block:: bash

        $ twootfeed_create_mastodon_cli

    .. warning::
      | It may be necessary to temporarily disable two-factor authentication in your Mastodon account, if enabled.


- Generate the token to access feeds

.. versionadded:: 0.7.0

Since **twootfeed** is connected to the user account (personal API keys), feeds may display items with **restricted visibility** (like private toots or direct messages).

A token is now mandatory to start the application and access feeds, to limit exposing private items (feeds should **not** be publicly available).

Some examples for token generation (minimum length: 25 characters):

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

After generation, copy the value into  **'config.yml'**.

.. warning::
  | If the token is missing or invalid, **twootfeed** will not start.

- The files location and settings can be changed by exporting the following environment variables:

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

    (.venv) $ twootfeed


Upgrade
~~~~~~~

- Activate the virtualenv

.. code-block:: bash

    $ source .venv/bin/activate

- Upgrade with pip

.. code-block:: bash

    (.venv) $ pip install -U twootfeed

- Restart the application


Systemd service
~~~~~~~~~~~~~~~

To create a Linux service with systemd:

- create a service file:

.. code-block:: bash

    $ sudo nano /etc/systemd/system/twootfeed.service

Template (to update depending on your distribution and installation):

.. code-block::

    [Unit]
    Description=twootfeed service
    After=network.target
    StartLimitIntervalSec=0

    [Service]
    Type=simple
    Restart=always
    RestartSec=1
    User=<USER>
    #Environment="TWOOTFEED_CONFIG_DIR="
    #Environment="TWOOTFEED_CONFIG_FILE="
    #Environment="TWOOTFEED_LOG="
    #Environment="TWOOTFEED_SETTINGS="
    ExecStart=<TWOOTFEED_DIRECTORY>/.venv/bin/python3 -m twootfeed

    [Install]
    WantedBy=multi-user.target


- start the service:

.. code-block:: bash

    $ sudo systemctl start twootfeed

- to start on boot:

.. code-block:: bash

    $ sudo systemctl enable twootfeed


Usage
~~~~~

.. versionchanged:: 0.7.0

The following RSS feeds are available:

- for Twitter search:

    - http://localhost:8080/tweets?q=<query>&token=<token>

- for Mastodon search:

    - hashtag:

        - http://localhost:8080/toots/tags/<hashtag>?token=<token> (without the leading #)

    - query:

        - http://localhost:8080/toots/search?q=<query>&token=<token>

- for Mastodon user favorites:

    - http://localhost:8080/toots/favorites?token=<token>

- for Mastodon user bookmarks:

    - http://localhost:8080/toots/bookmarks?token=<token>

- for Mastodon user home timeline:

    - http://localhost:8080/toots/home_timeline?token=<token>

where ``<token>`` is the token set in configuration.