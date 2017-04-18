# python-twittfeed
**Python script to generate a rss feed from parsed twitter search, using Flask.**  
  
The RSS feed displays only the original tweets (not the retweets) and :
- links to :  
-- the original tweet on Twitter  
-- hashtags  
-- usernames  
- URLs 
- images
- source
- location
- numbers of retweets and favorites  
(see example below).  
  
  
## **Requirements :**
- Python 3 (tested with 3.6)
- [Flask](http://flask.pocoo.org/)
- [Feedgenerator](https://pypi.python.org/pypi/feedgenerator)
- [Tweepy](https://github.com/tweepy/tweepy)
- [pytz](https://pypi.python.org/pypi/pytz/)
- API keys from https://dev.twitter.com/  
  
  
## **Steps :**
- install flask, feedgenerator, tweepy and pytz packages :
```bash
$ pip3 install flask tweepy pytz feedgenerator
```

- clone this repo :
```bash
$ git clone https://github.com/SamR1/python-twittfeed.git
```

- copy/paste the Twitter API key values in **config.yml.example** and rename it **config.yml**.

- after starting server, the RSS feed is available on this url :  http://localhost:5000/_keywords_
```bash
$ export FLASK_APP=server.py
$ python3 -m flask run --host=0.0.0.0
```


*Example :*  
Search on Twitter :  
![Twitter search](images/twitter.png)  

Results in RSS Feed :  
![RSS Feed](images/RSSFeed.png)  
  
Display on FreshRSS, a great free self-hosted aggregator (https://github.com/FreshRSS/FreshRSS):    
![FreshRSS](images/FreshRSS.png)  
  

## **Todo :**
- [ ] handle the tweeperror "Rate limit exceeded" #2
