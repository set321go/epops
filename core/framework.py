import logging

import time
import yaml

from core.config import YamlConfigs
from core.extensions.manager import ExtManager


class Framework(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.configs = YamlConfigs(self.__load_yaml())
        self.ext_manager = ExtManager(self.configs)
        self.ext_manager.ext_manager_init()

    def __load_yaml(self):
        loaded_config = []

        logging.info("About to load configuration at %s", self.config_file)
        with open(self.config_file, 'r') as stream:
            try:
                for data in yaml.load_all(stream):
                    loaded_config.append(data)
            except yaml.YAMLError as exc:
                logging.exception('Unable to Load configuration')

        return loaded_config

    def start(self):
        logging.info("Starting...")
        for processor in self.ext_manager.get_new_processors():
            processor.run()

        try:
            while True:
                time.sleep(10)
                for processor in self.ext_manager.get_new_processors():
                    processor.run()
        except KeyboardInterrupt:
            logging.critical("Shutting down...")
