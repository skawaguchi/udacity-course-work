# Udacity Project 1

## Building the Project JavaScript
This project uses ES6 and so it needs to be transpiles to run in most browsers.
This decision was made because the author needed to familiarize himself with
ES6 and WebPack for work.

To compile the JavaScript code:

1. Ensure you that you have Node 0.12.x+. If you don't already, consider using
[`nvm`](https://github.com/creationix/nvm).
1. Run `npm install` from the project root.
1. Run `gulp webpack` or `npm start` to transpile the application code.

## Compiling Fresh Tomatoes
To create the stand-alone HTML file for the Fresh Tomatoes app, simply run
`python fresh_tomatoes.py` from the project root. You should see the
fresh_tomatoes.html file get gnerated. Simply open that in a browser to view
the application. 
