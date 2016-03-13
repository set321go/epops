import logging


class YamlConfigs(object):
    def __init__(self, configs):
        self.configs = self.__parse_config_ids(configs)

    @staticmethod
    def __parse_config_ids(configs):
        loaded_configs = {}
        for config in configs:
            if config['id']:
                loaded_configs[config['id']] = config
            else:
                logging.warning("A document was found in the yaml with no id property, unable to load")

        return loaded_configs

    def get_config(self, config_id):
        logging.debug("Get config with id: %s", config_id)

        if config_id in self.configs:
            return self.configs[config_id]
        else:
            logging.warning('No config found with id: %s', config_id)
            return {}
