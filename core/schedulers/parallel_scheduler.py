import collections

from core.processor.processor import Processor
from core.schedulers.scheduler import Scheduler


class ParallelScheduler(Scheduler, Processor):
    def __str__(self):
        return "Parallel Scheduler with: %s" % self.tasks

    def __init__(self):
        self.tasks = collections.deque()

    def run(self):
        super().run()

    def add_task(self, task):
        super().add_task(task)