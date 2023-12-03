# Method chaining -  use to call several methods on the same instance one after the other in a sequence of method calls.

class Pizza:

    def __init__(self) -> None:
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
        return self 
    
    def show_toppings(self):
        for topping in self.toppings:
            print(topping.capitalize())


pizza = Pizza()

pizza.add_topping("Mushrooms")\
     .add_topping("Brocolli")\
     .add_topping("Zuccini")\
     .add_topping("Olives")\
     .add_topping("Bell Pepper")\
     .show_toppings()