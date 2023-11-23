class BackPack:

    max_num_items = 10 #this attribute belongs to the class not to instance

    def __init__(self) -> None:
        self.items = []

my_backpack = BackPack()
your_backpack = BackPack()

print(my_backpack.max_num_items)
print(your_backpack.max_num_items)

print(BackPack.max_num_items)