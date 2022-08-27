# python-twootfeed
**generate an RSS feed from parsed Twitter or Mastodon search and Mastodon bookmarks/favorites/home timeline**  
  
[![PyPI version](https://img.shields.io/pypi/v/twootfeed.svg)](https://pypi.org/project/twootfeed/)
[![Downloads](https://pepy.tech/badge/twootfeed)](https://pepy.tech/project/twootfeed)
[![Python Version](https://img.shields.io/badge/python-3.7+-brightgreen.svg)](https://python.org) 
[![Flask Version](https://img.shields.io/badge/flask-2.2-brightgreen.svg)](http://flask.pocoo.org/)
[![code style: black](https://img.shields.io/badge/code%20style-black-black)](https://black.readthedocs.io/en/stable/) 
[![type check: mypy](https://img.shields.io/badge/type%20check-mypy-blue)](http://mypy-lang.org/)  
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/14d1c00121c04cd2b81453c597639ca6)](https://www.codacy.com/app/SamR1/python-twootfeed) 
[![Coverage Status](https://coveralls.io/repos/github/SamR1/python-twootfeed/badge.svg?branch=master)](https://coveralls.io/github/SamR1/python-twootfeed?branch=master) 
[![pipeline status](https://gitlab.com/SamR1/python-twootfeed/badges/master/pipeline.svg)](https://gitlab.com/SamR1/python-twootfeed/commits/master)

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
- visibility (only for Mastodon)
- numbers of retweets and likes for tweets and boosts and favourites for toots   


➡️ see [documentation](https://samr1.github.io/python-twootfeed/index.html) for installation instructions and features.  


## Contributors
Thanks to:
- [georgedorn](https://github.com/georgedorn) for adding:
  - rss feed generation with authenticated user's favorites
  - script to register the app and generate credentials for Mastodon
