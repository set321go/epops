import logging

import yaml

from core.config import YamlConfigs


class Framework(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.configs = YamlConfigs(self.__load_yaml())

    def __load_yaml(self):
        with open(self.config_file, 'r') as stream:
            try:
                return yaml.load_all(stream)
            except yaml.YAMLError as exc:
                logging.exception('Unable to Load configuration')
