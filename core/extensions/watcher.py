from watchdog.events import PatternMatchingEventHandler
import os.path


class FileWatcher(PatternMatchingEventHandler):
    def __init__(self, ext_manager):
        super().__init__(['*.zip'])
        self.ext_manager = ext_manager

    def on_created(self, event):
        self.ext_manager.new_plugin(os.path.basename(event.src_path))
