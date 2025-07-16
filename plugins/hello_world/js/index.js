window.PluginRegistry.registerRoute({
  path: '/hello-world',
  element: React.createElement(HelloWorld)
});
window.PluginRegistry.registerWidget({
  name: 'HelloWorld',
  path: '/hello-world'
});
function HelloWorld() {
  return /*#__PURE__*/React.createElement("div", null, /*#__PURE__*/React.createElement("h1", null, "Hello World!"), /*#__PURE__*/React.createElement("p", null, "This is a simple React component."));
}