# Setters are methods that we can call to set the value of an instance attribute 

# With setters we can validate the new value before assiging it to the attribute

class Dog:

    def __init__(self, name, age) -> None:
        self._name = name
        self.age = age

    def get_name(self):
        return self._name 
    
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            print("please enter a valid name")


my_dog = Dog("Nora", 8)

print("My dog is :", my_dog.get_name())

my_dog.set_name("Norita56")

print("My dog's new name is :", my_dog.get_name())