# Change log

## Version 0.7.0 (2022/07/16)

#### Misc
* [PR#31](https://github.com/SamR1/python-twootfeed/pull/31) - Minor improvements


## Version 0.7.0 (2022/07/15)

#### New Features

* [PR#29](https://github.com/SamR1/python-twootfeed/pull/29) - Add token to access feeds ⚠️ **breaking changes**
* [PR#28](https://github.com/SamR1/python-twootfeed/pull/28) - Add Mastodon home timeline

#### Misc
* [PR#30](https://github.com/SamR1/python-twootfeed/pull/30) - URLs update ⚠️ **breaking changes**
* dependencies update


## Version 0.6.8 (2021/10/05)

#### Misc

* Update dependencies including **Tweepy** 4.0

Note: **twootfeed** still using **Twitter** API v1.1


## Version 0.6.7 (2020/03/15)

#### New Features

* [Issue 27](https://github.com/SamR1/python-twootfeed/issues/27) - generate documentation with sphinx
* [Issue 26](https://github.com/SamR1/python-twootfeed/issues/26) - [Mastodon] add feed with user's bookmarks

In this release 2 issue were closed.


## Version 0.6.6 (2019/10/20)

#### Misc

* Update dependencies


## Version 0.6.5 (2019/09/23)

#### Bugs Fixed

* [Issue 25](https://github.com/SamR1/python-twootfeed/issues/25) - toot_search route returns 404 error

In this release 1 issue was closed.


## Version 0.6.4 (2019/08/31)

#### Misc

* Update dependencies


## Version 0.6.3 (2019/05/05)

#### Bugs Fixed

* [Issue 24](https://github.com/SamR1/python-twootfeed/issues/24) - return the correct HTTP code status when no keys are provided

#### Misc

* Update dependencies

In this release 1 issue was closed.


## Version 0.6.2 (2019/01/26)

#### New Features

* [Issue 23](https://github.com/SamR1/python-twootfeed/issues/23) - [Mastodon] add a new search route
* [Issue 22](https://github.com/SamR1/python-twootfeed/issues/22) - The number of workers for the HTTP Server can be set
* [Issue 21](https://github.com/SamR1/python-twootfeed/issues/21) - [Mastodon] use pagination to get toots

In this release 3 issues were closed.


## Version 0.6.1 (2019/01/25)

#### New Features

* [Issue 19](https://github.com/SamR1/python-twootfeed/issues/19) - Change environment variables

#### Bugs Fixed

* [Issue 20](https://github.com/SamR1/python-twootfeed/issues/20) - Limit items in feed to avoid error or time-out
* [Issue 18](https://github.com/SamR1/python-twootfeed/issues/18) - [Mastodon] fix reference characters in items title

In this release 3 issues were closed.


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
