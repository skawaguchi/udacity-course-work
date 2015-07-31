/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};

/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {

/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;

/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};

/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);

/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;

/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}


/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;

/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;

/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";

/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';

	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { 'default': obj }; }

	var _FreshTomatoes = __webpack_require__(1);

	var _FreshTomatoes2 = _interopRequireDefault(_FreshTomatoes);

	(0, _FreshTomatoes2['default'])(window.movies);

/***/ },
/* 1 */
/***/ function(module, exports) {

	// Note to reviewer: I prefer a minimally commented style of coding as prefer
	// Bob Martin's recommendation. I'll add comments here since that's the
	// exercise, but will rely on the most obvious names to communicate intention.

	// Inject global jQuery via IIFE
	'use strict';

	Object.defineProperty(exports, '__esModule', {
	  value: true
	});
	var FreshTomatoes = (function ($) {

	  // The string template that we'll be using to call YouTube
	  var YOU_TUBE_URL = 'http://www.youtube.com/embed/{{trailerYouTubeId}}?autoplay=1&html5=1';

	  // Initialization
	  function FreshTomatoes() {
	    setUpModalHandlers();
	    setUpMovieTilePopover();
	    setUpMovieTileClickHandler();
	  }

	  function playTrailer(trailerYouTubeId) {
	    // Use regex to insert the youtube id into the url string
	    var sourceUrl = YOU_TUBE_URL.replace(/\{\{trailerYouTubeId\}\}/, trailerYouTubeId);

	    $('#trailer-video-container').empty().append($('<iframe></iframe>', {
	      'id': 'trailer-video',
	      'type': 'text-html',
	      'src': sourceUrl,
	      'frameborder': 0
	    }));

	    $('#trailer').modal();
	  }

	  function modalClicked() {
	    // Remove the src so the player itself gets removed, as this is the only
	    // reliable way to ensure the video stops playing in IE
	    $('#trailer-video-container').empty();
	  }

	  function movieTileClicked() {
	    var
	    // Store the DOM reference to minimize DOm calls
	    targetEl = $(this),
	        trailerYouTubeId = targetEl.attr('data-trailer-youtube-id');

	    playTrailer(trailerYouTubeId);
	  }

	  function setUpModalHandlers() {
	    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', modalClicked);
	  }

	  function setUpMovieTilePopover() {
	    // Bind the popover. Uses the markup for configuration and data.
	    $('.movie-tile a').popover();
	  }

	  function setUpMovieTileClickHandler() {
	    $(document).on('click', '.movie-tile a', movieTileClicked);
	  }

	  return FreshTomatoes;
	})(window.jQuery);

	exports['default'] = FreshTomatoes;
	module.exports = exports['default'];

/***/ }
/******/ ]);