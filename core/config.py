import logging


class YamlConfigs(object):
    def __init__(self, configs):
        self.configs = configs

    def get_config(self, config_id):
        if config_id in self.configs:
            return self.configs[config_id]
        else:
            logging.warning('No config found with id: %s', config_id)
            return {}
