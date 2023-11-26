class Movie:

    def __init__(self, title, rating) -> None:
        self._title = title 
        self.rating = rating

    #getter acts as intermediate layer to fetch non-public attributes
    def get_title(self):
        return self._title
    
my_movie = Movie("Terminator", 4.7)

print(my_movie.get_title())