class Backpack:

    def __init__(self) -> None:
        self._items = []

    @property
    def items(self):
        return self._items
    
    def add_multiple_items(self, items):
        for item in items:
            self.add_item(item)
    
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
    
    def show_items(self, sorted_list=False):
        if sorted_list:
            print(sorted(self._items))
        else:
            print(self._items)
    

backpack = Backpack()

print(backpack.items)
backpack.add_multiple_items(["Torch","Bottle","Candle","Snacks"])
print(backpack.items)