from django.conf.urls import patterns, url

urlpatterns = patterns('feed.views',
    url(r'^rssfeed/(.+)$', 'query_feed'),
)