from Plugin import PluginManager


@PluginManager.registerTo("UiRequest")
class UiRequestPlugin(object):
    def route(self, path):
        PluginManager.plugin_manager.log.debug("FIND ME IN LOG: log/debug.log !!!!!".format(path))
	return super(UiRequestPlugin, self).route(path)

