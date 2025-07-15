// A plugin registration system
const PluginRegistry = {
  routes: [],
  widgets: [],
  registerRoute(route: any) {
    this.routes.push(route);
  },
  registerWidget(widget: any) {
    this.widgets.push(widget);
  },
};

// Attach to window for plugin scripts
(window as any).PluginRegistry = PluginRegistry;

export { PluginRegistry };
