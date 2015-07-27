"""This module provides movie information to the fresh_tomatoes app."""

import media
import actor
import fresh_tomatoes

def populate_movies():
    """Populates a list of movies."""

    world_war_z = media.Movie(
        "World War Z",
        "A epidemiologist struggles to find the cure for the zombie virus "
        "battling against time",
        "https://upload.wikimedia.org/wikipedia/en/d/dc/World_War_Z_poster.jpg",
        "https://www.youtube.com/watch?v=M5Y_nOkFvbY",
        [
            actor.Actor("Brad", "Pitt")
        ],
        [
            "http://i.neoseeker.com/screenshots/MjYzLzUv/world_war_z_image_"
            "xQoBm.jpg",
            "http://i.neoseeker.com/screenshots/MjYzLzUv/world_war_z_image_"
            "nxbku.jpg",
            "http://i.neoseeker.com/screenshots/MjYzLzUv/world_war_z_image_"
            "ftFQ8.jpg"
        ],
        2013
    )

    zombieland = media.Movie(
        "Zombieland",
        "A zombie comedy about a band of zombie apocalypse survivors looking for a "
        "safe haven in the United States.",
        "https://upload.wikimedia.org/wikipedia/en/a/a3/Zombieland-poster.jpg",
        "https://www.youtube.com/watch?v=8m9EVP8X7N8",
        [
            actor.Actor("Woody", "Harrelson"),
            actor.Actor("Jesse", "Eisenberg"),
            actor.Actor("Emma", "Stone")
        ],
        [
            "http://i.neoseeker.com/screenshots/MjUwLzAv/zombieland_image_"
            "8DM5q.jpg",
            "http://i.neoseeker.com/screenshots/MjUwLzAv/zombieland_image_"
            "y3DN7.jpg",
            "http://i.neoseeker.com/screenshots/MjUwLzAv/zombieland_image_"
            "e2yFc.jpg"
        ],
        2009
    )

    shaun_of_the_dead = media.Movie(
        "Shaun of the Dead",
        "Friends fight their way through zombies in hilarious fashion.",
        "http://landmarktheatre.org/wp-content/uploads/2014/10/Shaun-of-the-Dead-"
        "Poster.jpg",
        "https://www.youtube.com/watch?v=yfDUv3ZjH2k",
        [
            actor.Actor("Simon", "Pegg"),
            actor.Actor("Nick", "Frost")
        ],
        [
            "http://i.neoseeker.com/screenshots/MzU1LzMv/shaun_of_the_dead_"
            "image_4WEgu.jpg",
            "http://i.neoseeker.com/screenshots/MzU1LzMv/shaun_of_the_dead_"
            "image_dqt5z.jpg",
            "http://i.neoseeker.com/screenshots/MzU1LzMv/shaun_of_the_dead_"
            "image_xWXLs.jpg"
        ],
        2004
    )

    twenty_eight_days_later = media.Movie(
        "28 Days Later",
        "A coma patient awakens to discover that infected cannibals have taken over"
        " London, and maybe the world.",
        "http://www.movierulz.to/wp-content/uploads/2013/07/28-Days-Later.jpg",
        "https://www.youtube.com/watch?v=c7ynwAgQlDQ",
        [
            actor.Actor("Cillian", "Murphy")
        ],
        [
            "http://i.neoseeker.com/screenshots/TW92aWVzL0hvcnJvcg==/28_days_"
            "later_image29.jpg",
            "http://i.neoseeker.com/screenshots/TW92aWVzL0hvcnJvcg==/28_days_"
            "later_image19.jpg",
            "http://i.neoseeker.com/screenshots/TW92aWVzL0hvcnJvcg==/28_days_"
            "later_image21.jpg"
        ],
        2002
    )

    dawn_of_the_dead_remake = media.Movie(
        "Dawn of the Dead",
        "A group of survivors takes refuge in a mall.",
        "https://upload.wikimedia.org/wikipedia/en/1/16/Dawn_of_the_Dead_2004_"
        "movie.jpg",
        "https://www.youtube.com/watch?v=rhsutNfvuAY",
        [
            actor.Actor("Sarah", "Polley"),
            actor.Actor("Ving", "Rhames")
        ],
        [
            "http://i.neoseeker.com/screenshots/NTQwLzIv/dawn_of_the_dead_2004_"
            "image_k7z1U.jpg",
            "http://i.neoseeker.com/screenshots/NTQwLzIv/dawn_of_the_dead_2004_"
            "image_Ab6WN.jpg",
            "http://i.neoseeker.com/screenshots/NTQwLzIv/dawn_of_the_dead_2004_"
            "image_SatYT.jpg"
        ],
        2004
    )

    dead_snow = media.Movie(
        "Dead Snow",
        "A group of Norweigan friends combats Nazi zombies.",
        "https://upload.wikimedia.org/wikipedia/en/1/11/Dodsno.jpg",
        "https://www.youtube.com/watch?v=lEQwEmeWnyI",
        [
            actor.Actor("Vegar", "Hoel"),
            actor.Actor("Charlotte", "Frogner")
        ],
        [
            "http://i.neoseeker.com/screenshots/OTMwLzMv/dead_snow_image_"
            "u8ucs.jpg",
            "http://i.neoseeker.com/screenshots/OTMwLzMv/dead_snow_image_"
            "ZznCV.jpg",
            "http://i.neoseeker.com/screenshots/OTMwLzMv/dead_snow_image_"
            "Fwqep.jpg"
        ],
        2009
    )

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
