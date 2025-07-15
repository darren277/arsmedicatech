// A plugin registration system
import { PluginRoute, PluginWidget } from './types';

const PluginRegistry = {
  routes: [] as PluginRoute[],
  widgets: [] as PluginWidget[],
  registerRoute(route: PluginRoute) {
    this.routes.push(route);
  },
  registerWidget(widget: PluginWidget) {
    this.widgets.push(widget);
  },
};

// Attach to window for plugin scripts
(window as any).PluginRegistry = PluginRegistry;

export { PluginRegistry };
