import { useEffect, useState } from 'react';
import { PluginRegistry } from '../pluginRegistry';
import { PluginRoute } from '../types';

export function usePluginRoutes(baseRoutes: PluginRoute[]) {
  const [routes, setRoutes] = useState([
    ...baseRoutes,
    ...PluginRegistry.routes,
  ]);

  useEffect(() => {
    const origRegisterRoute = PluginRegistry.registerRoute;
    PluginRegistry.registerRoute = route => {
      origRegisterRoute.call(PluginRegistry, route);
      setRoutes([...baseRoutes, ...PluginRegistry.routes]);
    };
    // In case plugins are loaded after mount
    setRoutes([...baseRoutes, ...PluginRegistry.routes]);
    return () => {
      PluginRegistry.registerRoute = origRegisterRoute;
    };
  }, [baseRoutes]);

  return routes;
}
