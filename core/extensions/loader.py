from yapsy.AutoInstallPluginManager import AutoInstallPluginManager
from yapsy.PluginManager import PluginManager
import os.path


class ExtensionLoader(object):
    def __init__(self, core_config):
        self.simple_plugin_manager = PluginManager()
        default_dir = os.path.join(os.path.expanduser("~"), "epops")
        self.simple_plugin_manager.setPluginPlaces(core_config.get('plugin_dir', [default_dir]))

        self.pluginManager = AutoInstallPluginManager(default_dir, self.simple_plugin_manager)

    def ext_init(self):
        self.simple_plugin_manager.collectPlugins()
        return self.simple_plugin_manager.getAllPlugins()

    def ext_load_new(self, filename):
        self.pluginManager.installFromZip(filename)
        self.simple_plugin_manager.collectPlugins()
        return self.simple_plugin_manager.getAllPlugins()
