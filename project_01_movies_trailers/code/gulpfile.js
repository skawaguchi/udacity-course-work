'use strict';

var gulp = require('gulp');
var gutil = require('gulp-util');
var webpack = require('webpack');

gulp.task('webpack', function (cb) {
  webpack({
    entry: './src/app',
    output: {
      filename: 'app.js',
      path: 'dist'
    },
    module: {
      loaders: [
        { test: /\.js$/, exclude: [/node_modules/], loader: 'babel' }
      ]
    },
    resolve: {
      extensions: ['', '.js']
    }
  }, function (err, stats) {
    if (err) {
      throw new gutil.PluginError('webpack', err);
    }
    gutil.log('[webpack]', stats.toString({
      // output options
    }));
    cb();
  });
});
