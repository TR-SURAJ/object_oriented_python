class Circle:

    def __init__(self,radius,color) -> None:
        self.radius = radius
        self.color = color

my_circle = Circle(5,"Blue")

print(my_circle.radius)
print(my_circle.color)

my_circle.radius = 10 
my_circle.color = "Red"

print(my_circle.radius)
print(my_circle.color)