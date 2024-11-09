const webpack = require("webpack");
const path = require("path");
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: path.resolve(__dirname, "./src/index.js"),
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: ["babel-loader"],
      },
      {
        test: /\.css$/,
        exclude: /(node_modules)/,
        use: [
          { loader: 'style-loader' },
          { loader: 'css-loader' },
        ],
      },
    ],
  },
  resolve: {
    extensions: ["*", ".js", ".jsx", ".css"],
  },
  // output: {path: path.resolve(__dirname, "./dist"), filename: "bundle.js",  publicPath: '/'},
  plugins: [new webpack.HotModuleReplacementPlugin(), new HtmlWebpackPlugin({template: './src/index.html'})],
  devServer: {
    static: path.resolve(__dirname, "./public"),
    hot: true,
    port: 3010
    // port: 5010
  },
};
