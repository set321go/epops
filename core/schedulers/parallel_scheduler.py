import collections
import logging
from queue import Queue
from threading import Thread

from core.processor.processor import IProcessor
from core.schedulers.scheduler import IScheduler


class ParallelIScheduler(IScheduler, IProcessor):
    def __str__(self):
        return "Parallel Scheduler with: %s" % self.tasks

    def __init__(self, thread_count):
        self.thread_count = thread_count
        self.tasks = Queue()

    def run(self):
        for i in range(self.thread_count):
            worker = Thread(target=do_run_tasks, args=(self.tasks,))
            worker.setDaemon(True)
            worker.start()

        self.tasks.join()

    def add_task(self, task):
        if task:
            self.tasks.put(task)


def do_run_tasks(tasks):
    while True:
        current_task = tasks.get()
        logging.warning("Starting task: %s", current_task)
        current_task.run()
        tasks.task_done()
