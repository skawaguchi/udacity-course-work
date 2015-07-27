import webbrowser
import os
import re
import json

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="styles/main.css">
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container"></div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div id="screenshot"></div>
    <ul class="movie-list">
      {movie_tiles}
    </ul>

    <!-- Movie Details -->
    <div id="movie-detail-container"></div>

    <script>
      // Add the movies to JavaScript to allow us to create a more dynamic
      // user experience.
      var movies = {movie_list}
    </script>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="src/polyfills.js"></script>
    <script src="src/app.js"></script>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<li class="movie-tile col-md-4">
    <a class="text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer" data-movie-id={movie_id}>
        <img src="{poster_image_url}" width="220" height="342">
        <h2 class="movie-title">{movie_title}</h2>
    </a>
</li>
'''

# A single actor template
actor_tile_content = '''
<li class="actor-tile text-center">{name}</li>
'''

def create_actor_tiles_content(actors):
    content = ''
    for actor in actors:
        content += actor_tile_content.format(name=actor.get_name())
    return content

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        actor_tiles = create_actor_tiles_content(
            actors=movie.actors
        )

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_id=movie.id,
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            actor_tiles=actor_tiles,
            year = movie.year
        )

    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(
    movie_tiles=create_movie_tiles_content(movies),
    movie_list=json.dumps(movies, default=lambda o: o.__dict__)
  )

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
