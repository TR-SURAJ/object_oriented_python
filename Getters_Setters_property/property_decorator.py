# A function that takes a function and extends its behavior without explicitly modifying it

class Movie:

    def __init__(self, title, rating) -> None:
        self.title = title
        self._rating = rating 

    @property
    def rating(self):
        print("Calling the getter")
        return self._rating
    
    @rating.setter
    def rating(self, new_rating):
        print("Calling the setter")
        if isinstance(new_rating, float) and 1.0 <= new_rating <= 5.0:
            self._rating = new_rating
        else:
            print("Please enter valid rating")
    
favorite_movie = Movie("Titanic", 4.3)
print(favorite_movie.rating)

favorite_movie.rating = 4.5
print(favorite_movie.rating)