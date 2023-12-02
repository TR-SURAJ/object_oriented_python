class Backpack:

    def __init__(self) -> None:
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please provide a valid item")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0
        
    def has_item(self, item):
        return item in self._items
    

backpack = Backpack()

backpack.add_item('Bottle')
backpack.add_item('Umbrella')
backpack.add_item('Cap')

print(backpack.items)
    
backpack.remove_item('Bottle')

print(backpack.items)

print(backpack.has_item('Cap'))
 