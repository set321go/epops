# -*- coding: utf-8 -*-
import argparse
import logging

from core.framework import Framework

defaultConfigFile = 'config.yaml'


def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(description="Do something.")
    parser.add_argument('-c', '--config', required=False, default=defaultConfigFile)
    args = parser.parse_args()

    framework = Framework(args.config)

    framework.start()
