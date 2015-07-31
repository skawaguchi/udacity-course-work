var FreshTomatoes = (function ($) {

  var
    privateData = new WeakMap(),
    privateObject = {};

  const
    YOU_TUBE_URL = 'http://www.youtube.com/embed/{{trailerYouTubeId}}?autoplay=1&html5=1';

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

    $('#trailer-video-container')
      .empty()
      .append($('<iframe></iframe>', {
        'id': 'trailer-video',
        'type': 'text-html',
        'src': sourceUrl,
        'frameborder': 0
      })
    );

    $('#trailer').modal();
  }

  function modalClicked() {
    // Remove the src so the player itself gets removed, as this is the only
    // reliable way to ensure the video stops playing in IE
    $('#trailer-video-container').empty();
  }

  function movieTileClicked() {
    var
      targetEl = $(this),
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

}(window.jQuery));

export default FreshTomatoes;
