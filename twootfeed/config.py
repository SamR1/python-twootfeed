import os

from twootfeed import param

if os.getenv('TWOOTFEED_SETTINGS') == 'TestingConfig':
    from twootfeed.tests.data import TEST_TOKEN

    param['feed']['token'] = TEST_TOKEN


class BaseConfig:
    """Base configuration"""

    DEBUG = False
    TESTING = False
    FEED_CONFIG = param['feed']


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    DEBUG = True


class TestingConfig(BaseConfig):
    """Testing configuration"""

    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration"""
