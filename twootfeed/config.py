import os
import secrets

from twootfeed import param

if os.getenv('TWOOTFEED_SETTINGS') == 'TestingConfig':
    param['feed']['token'] = secrets.token_urlsafe()


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
