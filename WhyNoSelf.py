""" We skip self in arguments because the value of self is assigned automatically by the Python interpreter behind the scenes when the code runs. 
Its value is a reference to the instance in memory. """ 

class House:
	
    def __init__(self, price):
        print(self) # New print statement
        self.price = price
 
my_house = House(14000)