"""This module provides movie information to the fresh_tomatoes app."""

import media
import actor
import fresh_tomatoes

def populate_movies():
    """Populates a list of movies."""

    world_war_z = media.Movie({
        "film_id": "tt0816711",
        "film_title": "World War Z",
        "film_synopsis":
            "A epidemiologist struggles to find the cure for the zombie virus "
            "battling against time",
        "film_poster_url":
            "https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster"
            ".jpg",
        "film_trailer_url": "https://www.youtube.com/watch?v=M5Y_nOkFvbY",
        "film_actors": [
            actor.Actor("Brad", "Pitt")
        ],
        "film_year": 2013
    })

    zombieland = media.Movie({
        "film_id": "tt127834",
        "film_title": "Zombieland",
        "film_synopsis":
            "A zombie comedy about a band of zombie apocalypse survivors "
            "looking for a safe haven in the United States.",
        "film_poster_url":
            "https://upload.wikimedia.org/wikipedia/en/a/a3/"
            "Zombieland-poster.jpg",
        "film_trailer_url": "https://www.youtube.com/watch?v=8m9EVP8X7N8",
        "film_actors": [
            actor.Actor("Woody", "Harrelson"),
            actor.Actor("Jesse", "Eisenberg"),
            actor.Actor("Emma", "Stone")
        ],
        "film_year": 2009
    })

    shaun_of_the_dead = media.Movie({
        "film_id": "tt0365748",
        "film_title": "Shaun of the Dead",
        "film_synopsis":
            "Friends fight their way through zombies in hilarious fashion.",
        "film_poster_url":
            "http://landmarktheatre.org/wp-content/uploads/"
            "2014/10/Shaun-of-the-Dead-Poster.jpg",
        "film_trailer_url": "https://www.youtube.com/watch?v=yfDUv3ZjH2k",
        "film_actors": [
            actor.Actor("Simon", "Pegg"),
            actor.Actor("Nick", "Frost")
        ],
        "film_year": 2004
    })

    twenty_eight_days_later = media.Movie({
        "film_id": "tt0289043",
        "film_title": "28 Days Later",
        "film_synopsis":
            "A coma patient awakens to discover that infected "
            "cannibals have taken over London, and maybe the world.",
        "film_poster_url":
            "http://www.movierulz.to/wp-content/uploads/2013/"
            "07/28-Days-Later.jpg",
        "film_trailer_url": "https://www.youtube.com/watch?v=c7ynwAgQlDQ",
        "film_actors": [
            actor.Actor("Cillian", "Murphy")
        ],
        "film_year": 2002
    })

    dawn_of_the_dead_remake = media.Movie({
        "film_id": "tt0363547",
        "film_title": "Dawn of the Dead",
        "film_synopsis":
            "A group of survivors takes refuge in a mall.",
        "film_poster_url":
            "https://upload.wikimedia.org/wikipedia/en/1/16/"
            "Dawn_of_the_Dead_2004_movie.jpg",
        "film_trailer_url": "https://www.youtube.com/watch?v=rhsutNfvuAY",
        "film_actors": [
            actor.Actor("Sarah", "Polley"),
            actor.Actor("Ving", "Rhames")
        ],
        "film_year": 2004
    })

    dead_snow = media.Movie({
        "film_id": "tt127834",
        "film_title": "Dead Snow",
        "film_synopsis": "A group of Norweigan friends combats Nazi zombies.",
        "film_poster_url":
            "https://upload.wikimedia.org/wikipedia/en/1/11/"
            "Dodsno.jpg",
        "film_trailer_url": "https://www.youtube.com/watch?v=lEQwEmeWnyI",
        "film_actors": [
            actor.Actor("Vegar", "Hoel"),
            actor.Actor("Charlotte", "Frogner")
        ],
        "film_year": 2009
    })

    # Return the list of the movies to be rendered on the webpage
    return [
        world_war_z,
        zombieland,
        shaun_of_the_dead,
        twenty_eight_days_later,
        dawn_of_the_dead_remake,
        dead_snow
    ]

def show_movies(movies):
    """Populates a list of movies."""

    # Open the movie page with our movies in it
    fresh_tomatoes.open_movies_page(movies)

show_movies(populate_movies())
