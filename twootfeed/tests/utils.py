from typing import Any, Dict, List


# source: https://stackoverflow.com/a/32107024
class ToDotNotation(dict):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(ToDotNotation, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = ToDotNotation(v) if isinstance(v, dict) else v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = ToDotNotation(v) if isinstance(v, dict) else v

    def __getattr__(self, attr: str) -> Any:
        return self.get(attr)

    def __setattr__(self, key: str, value: Any) -> None:
        self.__setitem__(key, value)

    def __setitem__(self, key: str, value: Any) -> None:
        super(ToDotNotation, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item: Any) -> None:
        self.__delitem__(item)

    def __delitem__(self, key: str) -> None:
        super(ToDotNotation, self).__delitem__(key)
        del self.__dict__[key]


class ToDotNotationTweepy(ToDotNotation):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(ToDotNotation, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = ToDotNotation(v) if isinstance(v, dict) else v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = ToDotNotation(v) if isinstance(v, dict) else v


class Tweepy:
    def __init__(self, tweets: List):
        self.tweet_pages = self.items_in_pages(tweets)
        self.tweets = [ToDotNotationTweepy(tweet) for tweet in tweets]

    def Cursor(self, *args: Any, **kwargs: Any) -> 'Tweepy':
        return self

    def pages(self) -> List[List[ToDotNotationTweepy]]:
        return self.tweet_pages

    def items(self) -> List:
        return self.tweets

    @staticmethod
    def items_in_pages(tweets: List[Dict]) -> List[List[ToDotNotationTweepy]]:
        pages = []
        current_page = []
        for tweet_index, tweet in enumerate(tweets):
            current_page.append(ToDotNotationTweepy(tweet))
            if tweet_index > 4 or tweet_index == len(tweets) - 1:
                pages.append(current_page)
                current_page = []
        return pages


class TwitterApi:
    def __init__(self) -> None:
        self.search_tweets = True


class MastodonApi:
    def __init__(self, toots: List[Dict], limit: int = 10) -> None:
        self.toots = toots
        self.limit = limit - 1

    def return_result(self) -> List[Dict]:
        result = self.toots[: self.limit]
        del self.toots[: self.limit]
        return result

    def timeline_hashtag(self, query: str) -> List[Dict]:
        return self.return_result()

    def bookmarks(self) -> List[Dict]:
        return self.return_result()

    def favourites(self) -> List[Dict]:
        return self.return_result()

    def timeline_home(self) -> List[Dict]:
        return self.return_result()

    def fetch_next(self, toots: List[Dict]) -> List[Dict]:
        return self.return_result()

    def search(self, query: str, resolve: bool = False) -> Dict:
        return {
            'accounts': [],
            'hashtags': [],
            'statuses': self.toots,
        }
