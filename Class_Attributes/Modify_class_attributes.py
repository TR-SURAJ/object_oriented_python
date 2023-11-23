class Circle:

    radius = 5

    def __init__(self, color) -> None:
        self.color = color 

print(Circle.radius)

my_circle = Circle("Blue")
your_circle = Circle("Green")

print(my_circle.radius)
print(your_circle.radius)

Circle.radius = 10 

print(my_circle.radius)
print(your_circle.radius)