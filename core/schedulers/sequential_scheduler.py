import collections

from core.processor.processor import Processor
from core.schedulers.scheduler import Scheduler


class SequentialScheduler(Scheduler, Processor):
    def __init__(self):
        self.tasks = collections.deque()

    def add_task(self, task):
        super().add_task(task)

    def run(self):
        super().run()
