class Movie:

    id_counter = 1

    def __init__(self,title,rating) -> None:
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating 

        Movie.id_counter +=1

movie = Movie("Godzilla", 4.6)

your_movie = Movie("Batman", 4.7)

print(movie.id)
print(your_movie.id)