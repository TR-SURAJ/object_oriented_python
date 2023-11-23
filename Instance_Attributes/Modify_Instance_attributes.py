class Backpack:

    def __init__(self,color) -> None:
        self.items = []
        self.color = color 

my_backpack = Backpack("Blue")
your_backpack = Backpack("Red")

print(my_backpack.color)
print(your_backpack.color)

print("Changing color")
my_backpack.color = 'Green'

print(my_backpack.color)
print(your_backpack.color)