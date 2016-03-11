from unittest import TestCase
from unittest.mock import MagicMock

from core.schedulers.sequential_scheduler import SequentialScheduler


class SequentialSchedulerTestSuite(TestCase):

    def setUp(self):
        self.scheduler = SequentialScheduler()

    def test_add_tasks(self):
        mock_task = MagicMock()
        self.scheduler.add_task(mock_task)

        self.assertTrue(len(self.scheduler.tasks) == 1)

    def test_add_tasks_ensure_ordering(self):
        mock_first_task = MagicMock()
        mock_second_task = MagicMock()
        self.scheduler.add_task(mock_first_task)
        self.scheduler.add_task(mock_second_task)

        self.assertTrue(len(self.scheduler.tasks) == 2)
        self.assertEqual(self.scheduler.tasks.pop(), mock_first_task)
        self.assertEqual(self.scheduler.tasks.pop(), mock_second_task)

    def test_run_tasks(self):
        mock_first_task = MagicMock()
        mock_second_task = MagicMock()
        self.scheduler.add_task(mock_first_task)
        self.scheduler.add_task(mock_second_task)

        self.scheduler.run()

        mock_first_task.run.assert_called_with()
        mock_second_task.run.assert_called_with()
