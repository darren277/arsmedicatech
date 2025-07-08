const webpack = require('webpack');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const PORT = process.env.PORT || 80;

module.exports = {
  entry: path.resolve(__dirname, '../src/index.tsx'),
  module: {
    rules: [
      {
        test: /\.(js|jsx|ts|tsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            configFile: path.resolve(__dirname, './babel.config.js'), // 👈 explicit path
          },
        },
      },
      {
        test: /\.css$/,
        exclude: /(node_modules)/,
        use: [
          { loader: 'style-loader' },
          { loader: 'css-loader' },
          {
            loader: 'postcss-loader',
            options: {
              postcssOptions: {
                config: path.resolve(__dirname, './postcss.config.js'), // 👈 explicit path
              },
            },
          },
        ],
      },
    ],
  },
  resolve: {
    extensions: ['*', '.js', '.jsx', '.ts', '.tsx', '.css'],
  },
  output: {
    path: path.resolve(__dirname, './dist'),
    filename: 'bundle.js',
    publicPath: '/',
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new HtmlWebpackPlugin({ template: './src/index.html' }),
    new webpack.DefinePlugin({
      'process.env.API_URL': JSON.stringify(
        process.env.API_URL || 'http://127.0.0.1:3123'
      ),
      'process.env.NODE_ENV': JSON.stringify(
        process.env.NODE_ENV || 'development'
      ),
    }),
  ],
  devServer: {
    allowedHosts: 'all',
    static: path.resolve(__dirname, './public'),
    hot: true,
    port: PORT,
    historyApiFallback: true,
  },
};
