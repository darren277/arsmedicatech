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

export { PluginRegistry };
