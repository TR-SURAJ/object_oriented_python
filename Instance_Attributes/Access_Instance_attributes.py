class Movie:

    def __init__(self,title,year,language,rating) -> None:
        self.title = title
        self.year = year 
        self.language = language
        self.rating = rating 

favorite_movie = Movie("Predator","2002","English",4.6)

your_favorite_movie = Movie("Godzilla",2009,"English",4.7)

print(favorite_movie.title)
print(favorite_movie.year)
print(favorite_movie.language)
print(favorite_movie.rating)

print("Your favorite movie")
print(your_favorite_movie.title)
print(your_favorite_movie.year)
print(your_favorite_movie.language)
print(your_favorite_movie.rating)