# -*- coding: utf-8 -*-
import os
import sys

import yaml

defaultConfigFile = 'config.yaml'


def main():
    configFile = sys.argv[1]

    if not os.path.exists(configFile):
        configFile = defaultConfigFile;
        print('No config file specified using default (config.yaml)')

    config = create_config(configFile)


def create_config(configFile):
    with open(configFile, 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
