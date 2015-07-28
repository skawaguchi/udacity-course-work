module.exports = function (config) {

  'use strict';

  config.set({

    autoWatch: true,

    // Normalize the reference to project root
    basePath: '../',

    files: [
      'http://code.jquery.com/jquery-1.10.1.min.js',
      'https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js',
      'test/specs/**/*.js',
      'src/**/*.js'
    ],

    browsers: ['PhantomJS2'],

    colors: true,

    coverageReporter: {
      type: 'lcov',
      dir: 'test/coverage'
    },

    exclude: [
      'src/polyfills.js'
    ],

    frameworks: ['jasmine'],

    //logLevel: config.LOG_ERROR,
    //logLevel: config.LOG_DEBUG,
    logLevel: config.LOG_INFO,

    // web server port
    port: 9876,

    preprocessors: {
      'src/**/*.js': 'coverage'
    },

    proxies: {
      '/': 'http://localhost:8086/'
    },

    reporters: ['coverage', 'spec'],

    singleRun: false,

    reportSlowerThan: 100
  });
};
