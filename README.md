# python-twootfeed
**Python script to generate a rss feed from parsed Twitter or Mastodon search and Mastodon favorites, using Flask.**  
  
[![Python Version](https://img.shields.io/badge/python-3.6-brightgreen.svg)](https://python.org) 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/14d1c00121c04cd2b81453c597639ca6)](https://www.codacy.com/app/SamR1/python-twootfeed)
[![Coverage Status](https://coveralls.io/repos/github/SamR1/python-twootfeed/badge.svg?branch=master)](https://coveralls.io/github/SamR1/python-twootfeed?branch=master)
[![Build Status](https://travis-ci.org/SamR1/python-twootfeed.svg?branch=master)](https://travis-ci.org/SamR1/python-twootfeed)
 
The RSS feed displays only the original tweets (not the retweets) and :
- links to :  
  - the original tweet on Twitter or toot on Mastodon  
  - hashtags  
  - usernames  
- URLs 
- images
- source
- location  (only for Twitter)
- numbers of retweets (or boosts for Mastodon) and favorites  
(see examples below).  

## **Requirements :**
- Python 3 (tested with 3.6)
- [Flask](http://flask.pocoo.org/)
- [Feedgenerator](https://pypi.python.org/pypi/feedgenerator)
- [Tweepy](https://github.com/tweepy/tweepy) (only tested with the [Twitter Standard API](https://developer.twitter.com/en/docs/tweets/search/overview/standard.html))
- [Mastodon.py](https://github.com/halcy/Mastodon.py)
- [pytz](https://pypi.python.org/pypi/pytz/)
- [PyYAML](https://github.com/yaml/pyyaml)
- [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4)
- [gunicorn](https://gunicorn.org/)
- API keys Twitter and/or Mastodon 
  
  
## **Steps :**
- Clone this repo :
  - dev environment
  ```bash
  $ git clone https://github.com/SamR1/python-twootfeed.git
  ```
  - production environment
  ```bash
  $ wget https://github.com/SamR1/python-twootfeed/archive/v0.5.1.tar.gz
  $ tar -xzf v0.5.1.tar.gz
  $ mv python-twootfeed-0.5.1 python-twootfeed
  ```

- Install Python virtualenv and packages
```bash
$ cd python-twootfeed
$ make install
```

- Fill in fields for the client(s) you will use in **python-twootfeed/config.yml** (see next step for API keys).

- Get API Keys
    - for **Twitter** : see https://apps.twitter.com  
    copy/paste the Twitter API key values in **config.yml** file ('_consumerKey_' and '_consumerSecret_')
    - for **Mastodon** : see [Python wrapper for the Mastodon API](https://mastodonpy.readthedocs.io/)  
    use the included script which will register your app and prompt you to log in, creating the credential files for you.
    ```bash
    $ make create-mastodon-cli
    ```

- Start the server
  - dev environment
  ```bash
  $ make serve
  ```
  - production environment
  ```bash
  $ make run
  ```

- The RSS feeds are available on these urls :  
   - for Twitter : http://localhost:5000/_keywords_ or http://localhost:5000/tweets/_keywords_
   - for Mastodon : http://localhost:5000/toots/_keywords_ (search) and http://localhost:5000/toot_favorites (favorites toots for connected user)

## Examples :  
### Search on Twitter :  
![Twitter search](images/twitter.png)  

Results in RSS Feed :  
![RSS Feed](images/RSSFeed.png)  
  
Display on FreshRSS, a great free self-hosted aggregator (https://github.com/FreshRSS/FreshRSS):    
![FreshRSS](images/FreshRSS.png)  

### Search on Mastodon : 
![Mastodon search](images/mastodon.png)

Results in RSS Feed :  
![Mastodon Feed](images/MastodonRSSFeed.png) 

Display on FreshRSS :
![Mastodon FreshRSS](images/MastodonFreshRSS.png)  
