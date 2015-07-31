// Note to reviewer: I prefer a minimally commented style of coding as prefer
// Bob Martin's recommendation. I'll add comments here since that's the
// exercise, but will rely on the most obvious names to communicate intention.

// Inject global jQuery via IIFE
var FreshTomatoes = (function ($) {

  // The string template that we'll be using to call YouTube
  const
    YOU_TUBE_URL = 'http://www.youtube.com/embed/{{trailerYouTubeId}}?autoplay=1&html5=1';

  // Initialization
  function FreshTomatoes() {
    setUpModalHandlers();
    setUpMovieTilePopover();
    setUpMovieTileClickHandler();
  }

  function playTrailer(trailerYouTubeId) {
    // Use regex to insert the youtube id into the url string
    var sourceUrl = YOU_TUBE_URL.replace(
      /\{\{trailerYouTubeId\}\}/,
      trailerYouTubeId
    );

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
      // Store the DOM reference to minimize DOm calls
      targetEl = $(this),
      trailerYouTubeId = targetEl.attr('data-trailer-youtube-id');

    playTrailer(trailerYouTubeId);
  }

  function setUpModalHandlers() {
    $(document).on(
      'click',
      '.hanging-close, .modal-backdrop, .modal',
      modalClicked
    );
  }

  function setUpMovieTilePopover() {
    // Bind the popover. Uses the markup for configuration and data.
    $('.movie-tile a').popover();
  }

  function setUpMovieTileClickHandler() {
    $(document).on('click', '.movie-tile a', movieTileClicked);
  }

  return FreshTomatoes;

}(window.jQuery));

export default FreshTomatoes;
