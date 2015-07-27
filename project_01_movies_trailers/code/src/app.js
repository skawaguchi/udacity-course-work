
var freshTomatoes = (function () {
  'use strict';

  var
    trailerVideoContainer = $('#trailer-video-container'),
    movieDetailContainer = $('#movie-detail-container');

  function init () {

    // Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        trailerVideoContainer.empty();
    });

    $(document).on('mouseover', '.movie-tile a', function (event) {
        var movieId = $(this).attr('data-movie-id');
        showMovieDetails(movieId);
    });

    // Start playing the video whenever the trailer modal is opened
    $(document).on('click', '.movie-tile a', function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id');
        playTrailer(trailerYouTubeId);
    });

  }

  function playTrailer (trailerYouTubeId) {
    var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

    trailerVideoContainer
      .empty()
      .append($("<iframe></iframe>", {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
      })
    );
  }

  function showMovieDetails (movieId) {
    var movie = getMovieInfo(movieId);
    movieDetailContainer.html(
      '<h2>' + movie.title + '</h2>' +
      '<span>Year:</span> <span>' + movie.year + '</span>'
    );
  }

  function getMovieInfo (movieId) {
    return movies.find(function (movie) {
      if (movie.id === movieId) {
        return movie;
      }
    });
  }

  return {
    init: init
  };

}());

freshTomatoes.init();
