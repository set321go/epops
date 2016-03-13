# -*- coding: utf-8 -*-
import os
import sys

from core.framework import Framework

defaultConfigFile = 'config.yaml'


def main():
    configfile = sys.argv[0]

    if not os.path.exists(configfile):
        configfile = 'config.yaml'
        print('No config file specified using default (config.yaml)')

    framework = Framework(configfile)

    framework.start()
