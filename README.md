# python-twootfeed
**generate a rss feed from parsed Twitter or Mastodon search and Mastodon favorites**  
  
[![PyPI version](https://img.shields.io/pypi/v/twootfeed.svg)](https://pypi.org/project/twootfeed/)
[![Downloads](https://pepy.tech/badge/twootfeed)](https://pepy.tech/project/twootfeed)
[![Python Version](https://img.shields.io/badge/python-3.6+-brightgreen.svg)](https://python.org) 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/14d1c00121c04cd2b81453c597639ca6)](https://www.codacy.com/app/SamR1/python-twootfeed) 
[![Coverage Status](https://coveralls.io/repos/github/SamR1/python-twootfeed/badge.svg?branch=master)](https://coveralls.io/github/SamR1/python-twootfeed?branch=master) 
[![Build Status](https://travis-ci.org/SamR1/python-twootfeed.svg?branch=master)](https://travis-ci.org/SamR1/python-twootfeed)

---

The RSS feed displays only the original tweets (not the retweets) and toots, with:
- links to :  
  - the tweet on Twitter or toot on Mastodon  
  - hashtags  
  - usernames  
- URLs 
- images
- source
- location (only for Twitter)
- numbers of retweets and likes for tweets and boosts and favourites for toots   
(see examples below).  

## Requirements

- Python 3.6+
- API keys Twitter and/or Mastodon 

  
## Installation and configuration

- Install from pip

```bash
$ pip install twootfeed
```

- Initialize the configuration file
```bash
$ twootfeed_init
```

- Fill in fields for the client(s) you will use in **'~/.config/twootfeed/config.yml'** :
  - for **Twitter** : see https://apps.twitter.com  
  copy/paste the Twitter API key values in **config.yml** file ('_consumerKey_' and '_consumerSecret_')
  - for **Mastodon** : see [Python wrapper for the Mastodon API](https://mastodonpy.readthedocs.io/)  
  use the included script which will register your app and prompt you to log in, creating the credential files for you.
  ```bash
  $ twootfeed_create_mastodon_cli
  ```
  Update the [feed and app parameters](https://github.com/SamR1/python-twootfeed/wiki/Application-parameters).

  
- The files location can be changed with the following environment variables:

| variable               | description                                   | app default value                                                                         |
|------------------------|-----------------------------------------------| ------------------------------------------------------------------------------------------|
| `TWOOTFEED_CONFIG_DIR` | configuration and credentials files directory | **'~/.config/twootfeed/'**                                                                |
| `TWOOTFEED_CONFIG_FILE`| config file full path                         | config dir + **'config.yml'** => with default value: **'~/.config/twootfeed/config.yml'** |
| `TWOOTFEED_LOG`        | application log file                          | _no default value (log printed on the console)_                                           |

- Start the app
```bash
$ twootfeed
```

## Usage 

The RSS feeds are available on these urls:  
  - for Twitter: http://localhost:8080/<keywords> or http://localhost:8080/tweets/<keywords>
  - for Mastodon: 
    - search:
        - keyword as a hashtag: http://localhost:8080/toots/<hashtag> (without the leading #)
        - query: http://localhost:8080/toot_search/<query>
    - connected user favourites: http://localhost:8080/toot_favorites


## Examples 

### Search on Twitter 

![Twitter search](https://raw.githubusercontent.com/SamR1/python-twootfeed/master/images/twitter.png)  

Results in RSS Feed:  
![RSS Feed](https://raw.githubusercontent.com/SamR1/python-twootfeed/master/images/RSSFeed.png)  
  
Display on FreshRSS, a great free self-hosted aggregator (https://github.com/FreshRSS/FreshRSS):   
![FreshRSS](https://raw.githubusercontent.com/SamR1/python-twootfeed/master/images/FreshRSS.png)  

### Search on Mastodon

![Mastodon search](https://raw.githubusercontent.com/SamR1/python-twootfeed/master/images/mastodon.png)

Results in RSS Feed:  
![Mastodon Feed](https://raw.githubusercontent.com/SamR1/python-twootfeed/master/images/MastodonRSSFeed.png) 

Display on FreshRSS:  
![Mastodon FreshRSS](https://raw.githubusercontent.com/SamR1/python-twootfeed/master/images/MastodonFreshRSS.png)  


## Contribute
see [Quick start for developers](https://github.com/SamR1/python-twootfeed/wiki/Quick-start-for-developers)


## Contributors
Thanks to:
- [georgedorn](https://github.com/georgedorn) for adding:
  - rss feed generation with authenticated user's favorites
  - script to register the app and generate credentials for Mastodon
