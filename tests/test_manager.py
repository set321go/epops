import os
from unittest import TestCase
from unittest.mock import MagicMock

from core.extensions.manager import ExtManager


class TestExtManager(TestCase):

    def setUp(self):
        self.config = MagicMock()
        self.config.get_config = MagicMock(returned_value={
            'plugin-dir': [os.path.join(os.path.curdir, 'tests', 'no-extensions')]}
        )
        self.manager = ExtManager(self.config)

    def test_ext_manager_init(self):
        self.assertTrue(self.manager)
