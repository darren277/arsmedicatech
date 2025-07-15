window.PluginRegistry.registerRoute({
  path: '/hello-world',
  element: React.createElement(HelloWorld),
});

window.PluginRegistry.registerWidget({
  name: 'HelloWorld',
  path: '/hello-world',
});

function HelloWorld() {
  return (
    <div>
      <h1>Hello World!</h1>
      <p>This is a simple React component.</p>
    </div>
  );
}
