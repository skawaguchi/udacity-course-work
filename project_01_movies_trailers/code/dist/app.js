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

	'use strict';

	Object.defineProperty(exports, '__esModule', {
	  value: true
	});
	var FreshTomatoes = (function ($) {

	  var privateData = new WeakMap(),
	      privateObject = {};

	  var YOU_TUBE_URL = 'http://www.youtube.com/embed/{{trailerYouTubeId}}?autoplay=1&html5=1';

	  function FreshTomatoes(movies) {
	    privateData.set(privateObject, {
	      movies: movies
	    });
	    setUpModalHandlers();
	    setUpMovieTilePopover();
	    setUpMovieTileClickHandler();
	  }

	  function playTrailer(trailerYouTubeId) {
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
	    var targetEl = $(this),
	        trailerYouTubeId = targetEl.attr('data-trailer-youtube-id');

	    playTrailer(trailerYouTubeId);
	  }

	  function setUpModalHandlers() {
	    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', modalClicked);
	  }

	  function setUpMovieTilePopover() {
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