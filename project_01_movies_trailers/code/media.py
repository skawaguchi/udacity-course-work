import webbrowser

class Movie():

    # Default to a 'no image' image instead of an ugly missing image or something
    NO_IMAGE_PATH="/img/no_image.png"

    # Bind all of the data associated with movies
    def __init__(self, film_id, film_title, film_synopsis, film_poster_url, film_trailer_url, film_actors, film_screenshots, film_year):

        self.id = film_id
        self.title = film_title
        self.synopsis = film_synopsis
        self.poster_image_url = film_poster_url
        self.trailer_youtube_url = film_trailer_url
        self.actors = film_actors
        self.screenshots = film_screenshots
        self.year = film_year

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
