# Change log

## Version 0.6.0 (2019/01/23)

#### New Features

* twootfeed is now available on PyPI

#### Bugs Fixed

* [Issue 17](https://github.com/SamR1/python-twootfeed/issues/17) - [Twitter] the name used in url is the display name and not the username

#### Misc
* Python 3.7 support (since Tweepy 3.7 support)
* Refactor
* Continuous integration and tests coverage

In this release 1 issue was closed.


## Version 0.5.1 (2018-10-17)

#### Misc
* Performance improvements (code refactoring)
* Use of Gunicorn for Production environments


## Version 0.5.0 - Mastodon extended support (2018-10-14)

#### New Features

* [Issue 10](https://github.com/SamR1/python-twootfeed/issues/10) - add Mastodon support

#### Bugs Fixed
* [Issue 16](https://github.com/SamR1/python-twootfeed/issues/16) - [Twitter] long tweets are truncated
* [Issue 15](https://github.com/SamR1/python-twootfeed/issues/15) - [Twitter] Images are no longer displayed
* [Issue 2](https://github.com/SamR1/python-twootfeed/issues/2) - handle the tweeperror "Rate limit exceeded"

#### Misc
* Major refactor

In this release 4 issues were closed.

  
## Version 0.4.0 - make support (2018-04-01)

#### Misc
* Adding Makefile to ease install and starting the server (see README)


## Version 0.3.0 - Mastodon favorites support (2017-12-07)

#### New Features
Thanks to @georgedorn for adding:
* [PR 14](https://github.com/SamR1/python-twootfeed/pull/14) - Mastodon Favorites feed, mastodon client script, refactor
  * rss feed generation with authenticated user's favorites
  * script to register the app and generate credentials for Mastodon


## Version 0.2.1 (2017-05-03)

#### Misc
* Minor fixes


## Version 0.2.0 (2017-04-18)

#### New Features
* [Issue 10](https://github.com/SamR1/python-twootfeed/issues/10) - add Mastodon support

In this release 1 issue was closed.


## Version 0.1.0 (2017-04-18)

#### New Features
* [Issue 4](https://github.com/SamR1/python-twootfeed/issues/4) - Using Flask instead of Django
* [Issue 3](https://github.com/SamR1/python-twootfeed/issues/3) - include query in RSS Feed Description
* [Issue 1](https://github.com/SamR1/python-twootfeed/issues/1) - externalize the Twitter API keys

#### Bugs Fixed
* [Issue 5](https://github.com/SamR1/python-twootfeed/issues/5) - display all media

In this release 4 issues were closed.
