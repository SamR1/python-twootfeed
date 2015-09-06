# django-twittfeed
**Python scripts using django to generate a rss feed from parsed twitter search.**  
  
The RSS feed displays only the original tweets (not the retweets) and :
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
- Django (tested on 1.7 and 1.8)  
Django tutorial : https://www.djangoproject.com/start/
- Tweepy : https://github.com/tweepy/tweepy
- pytz : https://pypi.python.org/pypi/pytz/
- API keys from https://dev.twitter.com/  
Create a new app and copy/paste the key values in **feed/views.py**.

## **Steps :**
- install django, tweepy and pytz packages :
```
$ pip install django tweepy pytz
```

- create a projet :
```
$ django-admin startproject twittfeed
```

- create an app :
```
$ django-admin startapp feed
```

- modify **[feed/views.py](https://github.com/SamR1/django-twittfeed/blob/master/feed/views.py)** to indicate the application keys

- upload **[twittfeed/urls.py](https://github.com/SamR1/django-twittfeed/blob/master/twittfeed/urls.py)**, **[feed/views.py](https://github.com/SamR1/django-twittfeed/blob/master/feed/views.py)** and **[feed/urls.py](https://github.com/SamR1/django-twittfeed/blob/master/feed/urls.py)**

- add 'feed' application in **twittfeed/settings.py**  
```
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feed'
)
```

- after starting server, the RSS feed is available on this url :  
http://localhost:8000/feed/rssfeed/keywords

*Example :* motogp honda lang:fr   
Search on Twitter :  
![Twitter search](https://raw.githubusercontent.com/SamR1/django-twittfeed/master/images/twitter.png)  

Results in RSS Feed :  
![RSS Feed](https://raw.githubusercontent.com/SamR1/django-twittfeed/master/images/RSSFeed.png)  
  
Display on FreshRSS, a great free self-hosted aggregator (https://github.com/FreshRSS/FreshRSS):    
![FreshRSS](https://raw.githubusercontent.com/SamR1/django-twittfeed/master/images/FreshRSS.png)  
  

## **Todo :**
- [ ] externalize the Twitter API keys (#1)
- [ ] handle the tweeperror "Rate limit exceeded" (#2)
- [ ] include query in RSS Feed Description (#3)
