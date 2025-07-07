const webpack = require("webpack");
const path = require("path");
const HtmlWebpackPlugin = require('html-webpack-plugin');

const PORT = process.env.PORT || 80;

module.exports = {
  entry: path.resolve(__dirname, "./src/index.tsx"),
  module: {
    rules: [
      {
        test: /\.(js|jsx|ts|tsx)$/,
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
    extensions: ["*", ".js", ".jsx", ".ts", ".tsx", ".css"],
  },
  output: {
    path: path.resolve(__dirname, "./dist"),
    filename: "bundle.js",
    publicPath: '/'
  },
  plugins: [new webpack.HotModuleReplacementPlugin(), new HtmlWebpackPlugin({template: './src/index.html'})],
  devServer: {
    allowedHosts: 'all',
    static: path.resolve(__dirname, "./public"),
    hot: true,
    port: PORT,
    historyApiFallback: true,
  },
};
