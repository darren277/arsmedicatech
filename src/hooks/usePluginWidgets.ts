import React, { useEffect } from 'react';
import { PluginRegistry } from '../pluginRegistry';

export function usePluginWidgets() {
  const [widgets, setWidgets] = React.useState([...PluginRegistry.widgets]);

  useEffect(() => {
    // Patch registerWidget to update state
    const origRegisterWidget = PluginRegistry.registerWidget;
    PluginRegistry.registerWidget = widget => {
      origRegisterWidget.call(PluginRegistry, widget);
      setWidgets([...PluginRegistry.widgets]);
    };
    // In case plugins are loaded after mount
    setWidgets([...PluginRegistry.widgets]);
    // Cleanup: restore original function
    return () => {
      PluginRegistry.registerWidget = origRegisterWidget;
    };
  }, []);

  return widgets;
}
