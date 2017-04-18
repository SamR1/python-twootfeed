# python-twittfeed
**Python script to generate a rss feed from parsed Twitter or Mastodon search, using Flask.**  
  
The RSS feed displays only the original tweets (not the retweets) and :
- links to :  
-- the original tweet on Twitter or toot on Mastodon
-- hashtags  
-- usernames  
- URLs 
- images (only for Twitter for now)
- source  (only for Twitter for now)
- location  (only for Twitter)
- numbers of retweets (or reblogs for Mastodon) and favorites  
(see example below).  
  
  
## **Requirements :**
- Python 3 (tested with 3.6)
- [Flask](http://flask.pocoo.org/)
- [Feedgenerator](https://pypi.python.org/pypi/feedgenerator)
- [Tweepy](https://github.com/tweepy/tweepy)
- [pytz](https://pypi.python.org/pypi/pytz/)
- [BeautifoulSoup](https://pypi.python.org/pypi/beautifulsoup4)
- [Mastodon.py](https://github.com/halcy/Mastodon.py)
- API keys Twitter and/or Mastodon 
  
  
## **Steps :**
- install Python packages : flask, BeautifoulSoup, Mastodon.py, feedgenerator, tweepy and pytz
```bash
$ pip3 install flask bs4 feedgenerator tweepy pytz Mastodon.py
```

- clone this repo :
```bash
$ git clone https://github.com/SamR1/python-twittfeed.git
```

- API Keys
    - for **Twitter** : see https://dev.twitter.com  
    copy/paste the Twitter API key values in **config.yml.example** ('_consumerKey_' and '_consumerSecret_')
    - for **Mastodon** : see [Python wrapper for the Mastodon](https://github.com/halcy/Mastodon.py)  
       - generate client and user credentials files :  
        ```python
        from mastodon import Mastodon
        
        # Register app - only once!        
        Mastodon.create_app(
             'pytooterapp',
              to_file = 'tootrss_clientcred.txt'
        )        
        
        # Log in - either every time, or use persisted        
        mastodon = Mastodon(client_id = 'pytooter_clientcred.txt')
        mastodon.log_in(
            'my_login_email@example.com',
            'incrediblygoodpassword',
            to_file = 'tootrss_usercred.txt'
        )
        ```
        - copy/paste file names in **config.yml.example** ('_client_id_file_' and '_access_token_file_')
        
Rename the config file **config.yml**.

- Start the server
```bash
$ export FLASK_APP=server.py
$ python3 -m flask run --host=0.0.0.0
```

- the RSS feeds are available on these urls :  
   - for Twitter : http://localhost:5000/_keywords_ or http://localhost:5000/tweets/_keywords_
   - for Mastodon : http://localhost:5000/toots/_keywords_

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

## **Todo :**
- [ ] handle the tweeperror "Rate limit exceeded" #2
- [ ] handle the different exceptions properly 