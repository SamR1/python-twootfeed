Features
########

Description
~~~~~~~~~~~

**twootfeed** generate an RSS feed from **Twitter** or **Mastodon** search and from **Mastodon** bookmarks/favorites/home timeline.

The feed displays only the original tweets (not the retweets) and toots, with:

- links to :

    - the tweet on Twitter or toot on Mastodon
    - hashtags
    - usernames

- URLs
- images
- source
- location (only for Twitter)
- numbers of retweets and likes for tweets and boosts and favourites for toots



.. danger::

   | **twootfeed** is developed for personal use.
   | Tweets and toots are displayed for the user associated to API keys, it may expose private items if feeds are publicly available.


Examples
~~~~~~~~

- Search on Twitter

.. figure:: _images/twitter.png
   :alt: Twitter search
   :figclass: doc-img

Results in RSS Feed:

.. figure:: _images/RSSFeed.png
   :alt: RSS Feed
   :figclass: doc-img

Display on FreshRSS, a great free self-hosted aggregator (https://github.com/FreshRSS/FreshRSS):

.. figure:: _images/FreshRSS.png
   :alt: FreshRSS
   :figclass: doc-img

- Search on Mastodon

.. figure:: _images/mastodon.png
   :alt: Mastodon search
   :figclass: doc-img

Results in RSS Feed:

.. figure:: _images/MastodonRSSFeed.png
   :alt: Mastodon Feed
   :figclass: doc-img

Display on FreshRSS:

.. figure:: _images/MastodonFreshRSS.png
   :alt: Mastodon FreshRSS
   :figclass: doc-img
