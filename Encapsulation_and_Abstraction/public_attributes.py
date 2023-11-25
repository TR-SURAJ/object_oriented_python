class Car:
    #public attributes can be accessed and modified outside of the class
    def __init__(self, brand, model, year) -> None:
        self.brand = brand 
        self.model = model 
        self.year = year 

my_car = Car("Tata Nexon", "SX AMT", 2023)

print(my_car.year)

#cons of making the attribute public, you can easily manipulate it
my_car.year = 5303
print(my_car.year)