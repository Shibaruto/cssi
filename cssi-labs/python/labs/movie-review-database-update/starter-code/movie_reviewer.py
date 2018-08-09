inside_movie = {
    "title": "Inside Out",
    "id": "tt2096673",
    "year_released": 2012,
    "rating": "PG",
    "score": 7.5,
    "out_of": 10,
    "reviews": 463787
}

inside_movie["year_released"] = 2015
inside_movie["score"] = 8.2
inside_movie["reviews"] = 492446

inside_movie.pop("out_of")

inside_movie["genre"] = ["animation", "adventure", "comedy"]

for i in inside_movie:
    print i, ":", inside_movie[i]

shrek_movie = {
    "title": "Inside Out",
    "id": "tt0126029",
    "year_released": 2001,
    "rating": "PG",
    "score": 7.9,
    "out_of": 10,
    "reviews": 531432,
    "genre": ["Animation", "Adventure", "Comedy"]
}

movies = [shrek_movie, inside_movie]

user = raw_input("Enter a genre: ").capitalize()

bestMovie = {"title": "none", "rating": 0}

for i in movies:
    if user in i["genre"]:
        if bestMovie["score"] < i["score"]:
            bestMovie["score"] = i["score"]
            bestMovie["title"] = i["title"]

print bestMovie["title"]
