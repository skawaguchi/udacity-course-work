import media
import fresh_tomatoes

world_war_z = media.Movie(
    "World War Z",
    "A epidemiologist struggles to find the cure for the zombie virus battling against time",
    "https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster.jpg",
    "https://www.youtube.com/watch?v=M5Y_nOkFvbY"
)

zombieland = media.Movie(
    "Zombieland",
    "A zombie comedy about a band of zombie apocalypse survivors looking for a safe haven in the United States.",
    "https://upload.wikimedia.org/wikipedia/en/a/a3/Zombieland-poster.jpg",
    "https://www.youtube.com/watch?v=8m9EVP8X7N8"
)

# Create the list of the movies to be rendered on the webpage
movies = [ world_war_z, zombieland ]

# Open the movie page with our movies in it
fresh_tomatoes.open_movies_page(movies)
