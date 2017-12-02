"""
Loads and parses the configuration file.
"""
import yaml

def get_config():
    with open('config.yml', 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
            sys.exit()
