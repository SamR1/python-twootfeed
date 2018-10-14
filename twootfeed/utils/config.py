import os

import yaml


def get_config():
    config_file = os.getenv('APP_CONFIG')
    with open(config_file, 'r', encoding='utf-8') as stream:
        return yaml.safe_load(stream)
