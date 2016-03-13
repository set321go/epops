from unittest import TestCase
from unittest.mock import MagicMock

from core.schedulers.parallel_scheduler import ParallelIScheduler


class ParallelSchedulerTestSuite(TestCase):

    def setUp(self):
        self.scheduler = ParallelIScheduler(5)

    def test_add_tasks(self):
        mock_task = MagicMock()
        self.scheduler.add_task(mock_task)

        self.assertTrue(self.scheduler.tasks.qsize() == 1)

    def test_run_tasks(self):
        mock_first_task = MagicMock()

        self.scheduler.add_task(mock_first_task)
        self.scheduler.add_task(mock_first_task)
        self.scheduler.add_task(mock_first_task)
        self.scheduler.add_task(mock_first_task)
        self.scheduler.add_task(mock_first_task)

        self.scheduler.run()

        mock_first_task.run.assert_called_with()
