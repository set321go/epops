import logging
import os.path

from core.extensions.loader import ExtensionLoader
from core.extensions.watcher import FileWatcher
from watchdog.observers import Observer


class ExtManager(object):
    def __init__(self, config):
        self.config = config
        default_dir = os.path.join(os.path.expanduser("~"), "epops")
        self.dir_path = self.config.get_config('core').get('plugin_dir', [default_dir])
        self.loader = ExtensionLoader(config.get_config('core'))
        self.watcher = FileWatcher(self)
        self.extensions = []

    def ext_manager_init(self):
        logging.info("Initializing the extension manager")
        self.extensions = self.loader.ext_init()
        logging.info("Loaded %i extensions", len(self.extensions))
        logging.debug("Finished loading plugins, watching plugin directory %s", self.dir_path[0])
        observer = Observer()
        observer.schedule(FileWatcher(self), path=self.dir_path[0])
        observer.start()

    def new_plugin(self, plugin_artifact):
        logging.info("New plugin found: %s", plugin_artifact)
        extension_set = set(self.loader.ext_load_new(plugin_artifact))
        new_extensions = [x for x in self.extensions if x not in extension_set]
        self.extensions.append(new_extensions)

    def get_processors(self):
        processors = []
        for extension in self.extensions:
            extension.plugin_object.activate()
            processors.extend(extension.plugin_object.get_tasks())

        return processors

