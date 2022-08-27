Features
########

Description
~~~~~~~~~~~

**twootfeed** generates an RSS feed from **Twitter** or **Mastodon** search and from **Mastodon** bookmarks/favorites/home timeline.

The feed displays only the original tweets (not the retweets) and toots, with:

- links to :

    - the tweet on Twitter or toot on Mastodon
    - hashtags
    - usernames

- URLs
- images, video (mp4) and animated gif (as mp4 video)
- image description (only for Mastodon)
- source if available
- location (only for Twitter)
- visibility (only for Mastodon)
- numbers of retweets and likes for tweets and boosts and favourites for toots

.. warning::

   | **twootfeed** is intended for personal use only.
   | Tweets and toots are displayed with the user account associated to the API keys (feeds may contain items with **restricted visibility**).

----------

.. figure:: _images/screenshot.png
   :alt: Mastodon search screenshot
   :figclass: doc-img

   Example: Mastodon search for hashtag **#twootfeed** displayed in `FreshRSS <https://www.freshrss.org/>`__