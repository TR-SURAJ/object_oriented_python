class Circle:

    def __init__(self, radius) -> None:
        self.radius = radius 

    def find_diameter(self):
        print(f"Diameter: {self.radius * 2} ")


circle = Circle(5)
circle.find_diameter()