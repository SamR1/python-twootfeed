from datetime import datetime


# source: https://stackoverflow.com/a/32107024
class ToDotNotation(dict):

    def __init__(self, *args, **kwargs):
        super(ToDotNotation, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = ToDotNotation(v) if isinstance(v, dict) else v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = ToDotNotation(v) if isinstance(v, dict) else v

    def __getattr__(self, attr):
        return (self[attr] if attr in ['full_text', 'retweeted_status']
                else self.get(attr))

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(ToDotNotation, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(ToDotNotation, self).__delitem__(key)
        del self.__dict__[key]


class ToDotNotationTweepy(ToDotNotation):

    def __init__(self, *args, **kwargs):
        super(ToDotNotation, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    if k == 'created_at':
                        v = v[:19] + v[25:]
                        self[k] = datetime.strptime(v, '%a %b %d %H:%M:%S %Y')
                    else:
                        self[k] = ToDotNotation(v) if isinstance(v, dict) else v  # noqa

        if kwargs:
            for k, v in kwargs.items():
                self[k] = ToDotNotation(v) if isinstance(v, dict) else v


class Tweepy:
    def __init__(self, tweets):
        self.tweets = [ToDotNotationTweepy(tweet) for tweet in tweets]

    def items(self):
        return self.tweets


class Api:
    def __init__(self):
        self.search = True
