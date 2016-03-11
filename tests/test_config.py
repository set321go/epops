# -*- coding: utf-8 -*-
from core.config import YamlConfigs

from unittest import TestCase

import yaml


class ConfigTestSuite(TestCase):
    """Config test cases."""

    def setUp(self):
        self.configs = yaml.load_all("""---
id: core
---
id: data
type: mysql
data_set: basic
---
id: installer
location: 10.10.1.1""")

    def test_create_configurations(self):
        result = YamlConfigs(self.configs)
        self.assert_(result)

    def test_get_existing_configuration(self):
        configs = YamlConfigs(self.configs)
        result = configs.get_config('core')
        self.assert_(result)
        self.assertEqual('core', result['id'])

    def test_get_missing_configuration(self):
        configs = YamlConfigs(self.configs)
        result = configs.get_config('sausage')
        self.assertFalse(result)
