module.exports = function (config) {

  'use strict';

  config.set({

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

    // exclude: [
    //   '**/*.e2e.js'
    // ],

    frameworks: ['jasmine'],

    //logLevel: config.LOG_ERROR,
    //logLevel: config.LOG_DEBUG,
    logLevel: config.LOG_DEBUG,

    // web server port
    port: 9876,

    preprocessors: {
      'test/specs/**/!(*.spec).js': 'coverage'
    },

    proxies: {
      '/': 'http://localhost:8086/'
    },

    reporters: ['coverage', 'spec'],

    singleRun: false,
    // ,

    reportSlowerThan: 100,
    //
    // // cli runner port
    // runnerPort: config.RUNNER_PORT || 8090,

    // urlRoot: '__karma'
  });
};
