# -*- coding: utf-8 -*-
import os.path
from unittest import TestCase

from core.extensions.loader import ExtensionLoader


class TestExtensionLoader(TestCase):

    def test_init_no_extensions(self):
        core_config = {'plugin_dir': [os.path.abspath("no-extensions")]}
        loader = ExtensionLoader(core_config)
        result = loader.ext_init()

        self.assertFalse(result)

    def test_init_with_extensions(self):
        core_config = {'plugin_dir': [os.path.abspath("extensions")]}
        loader = ExtensionLoader(core_config)
        result = loader.ext_init()

        self.assertTrue(result)
        self.assertEqual(1, len(result))

    def test_ext_load_new(self):
        core_config = {'plugin_dir': [os.path.abspath("zip-extensions")]}
        loader = ExtensionLoader(core_config)
        result = loader.ext_load_new('Archive.zip')

        self.assertTrue(result)
        self.assertEqual(1, len(result))
