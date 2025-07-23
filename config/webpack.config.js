const webpack = require('webpack');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const Dotenv = require('dotenv-webpack');

const PORT = process.env.PORT || 3012;

module.exports = (env = {}) => {
  const useDotenv = env.useDotenv === 'true' || env.useDotenv === true;

  const rules = [
    {
      test: /\.(js|jsx|ts|tsx)$/,
      exclude: /node_modules/,
      use: {
        loader: 'babel-loader',
        options: {
          configFile: path.resolve(__dirname, './babel.config.js'),
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
              config: path.resolve(__dirname, './postcss.config.js'),
            },
          },
        },
      ],
    },
    {
      test: /\.css$/,
      include: /node_modules/,
      use: ['style-loader', 'css-loader'],
    },
  ];

  const plugins = [
    new webpack.HotModuleReplacementPlugin(),
    new HtmlWebpackPlugin({ template: './src/index.html' }),
  ];

  if (useDotenv) {
    plugins.push(
      new Dotenv({
        path: path.resolve(__dirname, '../.env'),
      })
    );
    console.log('[webpack] [LOCAL] Using .env file via dotenv-webpack');
  } else {
    plugins.push(
      new webpack.DefinePlugin({
        'process.env.API_URL': JSON.stringify(
          process.env.API_URL || 'http://127.0.0.1:3123'
        ),
        'process.env.NODE_ENV': JSON.stringify(
          process.env.NODE_ENV || 'development'
        ),
        'process.env.SENTRY_DSN': JSON.stringify(process.env.SENTRY_DSN || ''),
      })
    );
    console.log('[webpack] [PROD] Using environment variables directly');
  }

  return {
    entry: path.resolve(__dirname, '../src/index.tsx'),
    module: {
      rules,
    },
    resolve: {
      extensions: ['*', '.js', '.jsx', '.ts', '.tsx', '.css'],
    },
    output: {
      path: path.resolve(__dirname, '../dist'),
      filename: 'bundle.js',
      publicPath: '/',
    },
    plugins,
    devServer: {
      allowedHosts: 'all',
      static: path.resolve(__dirname, './public'),
      hot: true,
      port: PORT,
      historyApiFallback: true,
    },
  };
};
