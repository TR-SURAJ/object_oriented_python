class Circle:
    # default arguments should be placed last
    def __init__(self, radius=5) -> None:
        self.radius = radius 

my_circle = Circle()
print(my_circle.radius)

your_circle = Circle(10)
print(your_circle.radius)