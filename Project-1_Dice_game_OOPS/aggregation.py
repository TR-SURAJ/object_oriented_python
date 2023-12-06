''' 
Aggregation - Concept in object-oriented programming that describes the relationship between two classes
It invloves building complex objects that are composed of other objects. It implies we store instances of the simpler objects in the 
more complex objects
It is a "has a" relationship between the classes. An object of class B has an object of class A

Ex: Employee "has a" Vechicle. Employee object will have instance of Vechile. Both are seperate objects
'''

class Vehicle:

    def __init__(self, color, license_plate, is_electric) -> None:
        self.color = color 
        self.license_plate = license_plate
        self.is_electric = is_electric

    def show_license_plate(self):
        print(self.license_plate)

    def show_info(self):
        print("My Vechile:")
        print(f"Color: {self.color}")
        print(f"License plate: {self.license_plate}")
        print(f"Electric: {self.is_electric}")



class Employee:

    def __init__(self, name, vehicle) -> None:
        self.name = name 
        self.vehicle = vehicle 

    def show_vehicle_info(self):
        self.vehicle.show_info()

    
vehicle = Vehicle("White", "KA-05-0236", is_electric=False)

employee = Employee("Suraj", vehicle)

print(employee.name)

print(employee.vehicle)

employee.show_vehicle_info()

print("---------------------------------------")
print(employee.vehicle.color)
print(employee.vehicle.license_plate)
print(employee.vehicle.is_electric)

employee.vehicle.show_license_plate()