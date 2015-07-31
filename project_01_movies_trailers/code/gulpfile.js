'use strict';

var gulp = require('gulp');
var gutil = require('gulp-util');
var path = require('path');
var karma = require('karma');
var karmaParseConfig = require('karma/lib/config').parseConfig;
var webpack = require('webpack');

function runKarma(configFilePath, options, cb) {

  configFilePath = path.resolve(configFilePath);

  var server = karma.server;
  var log = gutil.log;
  var colors = gutil.colors;
  var config = karmaParseConfig(configFilePath, {});

  Object.keys(options).forEach(function (key) {
    config[key] = options[key];
  });

  server.start(config, function (exitCode) {
    log('Karma has exited with ' + colors.red(exitCode));
    cb();
    // process.exit(exitCode);
    throw new Error('');
  });
}

/** actual tasks */

/** single run */
gulp.task('unit', function (cb) {
  runKarma('test/karma.conf.js', {}, cb);
});

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
