# python-twittfeed
**Python script to generate a rss feed from parsed twitter search, using Flask.**  
  
The RSS feed displays only the original tweets (not the retweets) and :
- links to :  
-- the original tweet on Twitter  
-- hashtags  
-- usernames  
- URLs 
- images
- numbers of retweets and favorites  
(see example below).  
  
  
## **Requirements :**
- Python 3 (tested with 3.6)
- Flask
- Tweepy : https://github.com/tweepy/tweepy
- pytz : https://pypi.python.org/pypi/pytz/
- API keys from https://dev.twitter.com/  
  
  
## **Steps :**
- install flask, tweepy and pytz packages :
```
$ pip3 install flask tweepy pytz
```

- clone this repo :
```
$ git clone https://github.com/SamR1/python-twittfeed.git
```

- copy/paste the Twitter API key values in **config.yml.example** and rename it **config.yml**.

- after starting server, the RSS feed is available on this url :  
http://localhost:5000/_keywords_

*Example :* motogp honda lang:fr  
Search on Twitter :  
![Twitter search](https://raw.githubusercontent.com/SamR1/django-twittfeed/master/images/twitter.png)  

Results in RSS Feed :  
![RSS Feed](https://raw.githubusercontent.com/SamR1/django-twittfeed/master/images/RSSFeed.png)  
  
Display on FreshRSS, a great free self-hosted aggregator (https://github.com/FreshRSS/FreshRSS):    
![FreshRSS](https://raw.githubusercontent.com/SamR1/django-twittfeed/master/images/FreshRSS.png)  
  

## **Todo :**
- [x] externalize the Twitter API keys #1
- [ ] handle the tweeperror "Rate limit exceeded" #2
- [x] include query in RSS Feed Description #3
