class Pizza:
    
    price = 12.99

    def __init__(self, description, toppings, crust) -> None:
        self.description = description
        self.toppings = toppings
        self.crust = crust 

print(Pizza.price)

my_pizza = Pizza("Veggie Feast", ["Mushrooms","brocolli","Zuccini"],"Wheat")
print(my_pizza.price)

Pizza.price = 13.99 
print(Pizza.price)
print(my_pizza.price)
