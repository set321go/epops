import collections
import logging

from core.processor.processor import Processor
from core.schedulers.scheduler import Scheduler


class SequentialScheduler(Scheduler, Processor):
    def __init__(self):
        self.tasks = collections.deque()

    def __str__(self):
        return "Scheduler with the following queue: %s" % self.tasks

    def add_task(self, task):
        if task:
            self.tasks.appendleft(task)

    def run(self):
        while self.tasks:
            current_task = self.tasks.pop()
            logging.info("Starting task: %s", current_task)
            current_task.run()
