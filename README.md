# django-twittfeed
**Python scripts using django to generate a rss feed from parsed twitter search.**  
  
The RSS feed displays obly the original tweets (not the retweets) and :
- links to :  
-- the original tweet on Twitter  
-- hashtags  
-- usernames  
- URLs 
- images
- numbers of retweets and favorites  
(see example below).  

Note : I'm new to Python and Django :smile:  
  
  
## **Prerequisites :**
- Python 3.4
- Django 1.8  
Django tutorial : https://www.djangoproject.com/start/
- Tweepy : https://github.com/tweepy/tweepy
- API keys from https://dev.twitter.com/  
Create a new app and copy/paste the key values in **feed/views.py**.

## **Steps :**
- install tweepy package :
```
$ pip install tweepy
```

- create a projet :
```
$ django-admin startproject twittfeed
```

- create an app :
```
$ django-admin startapp feed
```

- modify **feed/views.py** to indicate the application keys

- upload **twittfeed/urls.py**, **feed/views.py** and **feed/urls.py**

- after starting server, the RSS feed is available on this url :  
http://localhost:8000/feed/rssfeed/keywords

Example : motogp honda lang:fr   
![Twitter search](https://raw.githubusercontent.com/SamR1/django-twittfeed/master/images/twitter.png)  

![RSS Feed](https://raw.githubusercontent.com/SamR1/django-twittfeed/master/images/RSSFeed.png)  


## **Todo :**
- handle tweeperror "Rate limit exceeded"
