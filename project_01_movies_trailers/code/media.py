import webbrowser

class Movie():

    # Default to a 'no image' image instead of an ugly missing image or something
    NO_IMAGE_PATH="/img/no_image.png"

    def __init__(self, film_title, film_synopsis, film_poster_url, film_trailer_url):
        
        self.title = film_title
        self.synopsis = film_synopsis
        self.poster_image_url = film_poster_url
        self.trailer_youtube_url = film_trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)
