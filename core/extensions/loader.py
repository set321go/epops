from yapsy.AutoInstallPluginManager import AutoInstallPluginManager
from yapsy.PluginManager import PluginManager
import os.path

from core.extensions.extensions import IExtension


class ExtensionLoader(object):
    def __init__(self, core_config):
        default_dir = os.path.join(os.path.expanduser("~"), "epops")
        self.plugin_path = core_config.get('plugin_dir', [default_dir])
        self.simple_plugin_manager = PluginManager()
        self.simple_plugin_manager.setPluginPlaces(self.plugin_path)
        self.simple_plugin_manager.setPluginInfoExtension('plugin-meta')
        self.simple_plugin_manager.setCategoriesFilter({"Extension": IExtension})

        self.pluginManager = AutoInstallPluginManager(default_dir, self.simple_plugin_manager)
        self.pluginManager.setInstallDir(default_dir)

    def ext_init(self):
        self.simple_plugin_manager.collectPlugins()
        return self.simple_plugin_manager.getAllPlugins()

    def ext_load_new(self, filename):
        zip_path = os.path.join(self.plugin_path[0], filename)
        self.pluginManager.installFromZIP(zip_path)
        self.simple_plugin_manager.collectPlugins()
        return self.simple_plugin_manager.getAllPlugins()
