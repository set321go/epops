import os
from unittest import TestCase
from unittest.mock import MagicMock

from core.extensions.watcher import FileWatcher


class TestFileWatcher(TestCase):

    def setUp(self):
        self.mock_manager = MagicMock()
        self.watcher = FileWatcher(self.mock_manager)

    def test_create_event(self):
        mock_event = MagicMock()
        mock_event.src_path.return_value = 'test-path'

        self.watcher.on_created(mock_event)

        self.mock_manager.new_plugin.assert_called_with(os.path.basename(mock_event.src_path))
