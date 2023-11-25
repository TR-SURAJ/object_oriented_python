class Car:
    #
    def __init__(self, brand, model, year) -> None:
        self.brand = brand 
        self.model = model 
        self._year = year #making year non-public so that it is not manipulated

my_car = Car("Tata Nexon", "SX AMT", 2023)

print(my_car.year)

# No attribute is really private in python
my_car.year = 5303
print(my_car.year)

# AttributeError: 'Car' object has no attribute 'year'