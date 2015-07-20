import media
import actor
import fresh_tomatoes

world_war_z = media.Movie(
    "World War Z",
    "A epidemiologist struggles to find the cure for the zombie virus battling against time",
    "https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster.jpg",
    "https://www.youtube.com/watch?v=M5Y_nOkFvbY",
    [ actor.Actor("Brad", "Pitt")]
)

zombieland = media.Movie(
    "Zombieland",
    "A zombie comedy about a band of zombie apocalypse survivors looking for a safe haven in the United States.",
    "https://upload.wikimedia.org/wikipedia/en/a/a3/Zombieland-poster.jpg",
    "https://www.youtube.com/watch?v=8m9EVP8X7N8",
    [ actor.Actor("Woody", "Harrelson"), actor.Actor("Jesse", "Eisenberg"), actor.Actor("Emma", "Stone") ]
)

shaun_of_the_dead = media.Movie(
    "Shaun of the Dead",
    "Friends fight their way through zombies in hilarious fashion.",
    "http://landmarktheatre.org/wp-content/uploads/2014/10/Shaun-of-the-Dead-Poster.jpg",
    "https://www.youtube.com/watch?v=yfDUv3ZjH2k",
    [ actor.Actor("Simon", "Pegg"), actor.Actor("Nick", "Frost") ]
)

twenty_eight_days_later = media.Movie(
    "28 Days Later",
    "A coma patient awakens to discover that infected cannibals have taken over London, and maybe the world.",
    "http://www.movierulz.to/wp-content/uploads/2013/07/28-Days-Later.jpg",
    "https://www.youtube.com/watch?v=c7ynwAgQlDQ",
    [ actor.Actor("Cillian", "Murphy") ]
)

dawn_of_the_dead_2004 = media.Movie(
    "Dawn of the Dead",
    "A group of survivors takes refuge in a mall.",
    "https://upload.wikimedia.org/wikipedia/en/1/16/Dawn_of_the_Dead_2004_movie.jpg",
    "https://www.youtube.com/watch?v=rhsutNfvuAY",
    [ actor.Actor("Sarah", "Polley"), actor.Actor("Ving", "Rhames") ]
)

# Create the list of the movies to be rendered on the webpage
movies = [
    world_war_z,
    zombieland,
    shaun_of_the_dead,
    twenty_eight_days_later,
    dawn_of_the_dead_2004
]

# Open the movie page with our movies in it
fresh_tomatoes.open_movies_page(movies)
