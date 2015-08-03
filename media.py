"""Module related to movies."""

import webbrowser

class Movie(object):
    """Represents a movie object."""

    # Bind all of the data associated with movies
    def __init__(self, film):
        self.movie_id = film["film_id"]
        self.title = film["film_title"]
        self.synopsis = film["film_synopsis"]
        self.poster_image_url = film["film_poster_url"]
        self.trailer_youtube_url = film["film_trailer_url"]
        self.actors = film["film_actors"]
        self.year = film["film_year"]

    def show_trailer(self):
        """Tells the web browser to open a trailer."""
        webbrowser.open(self.trailer_youtube_url)

    def get_attr(self, attr):
        """Get a property of the movie."""
        return self[attr]
