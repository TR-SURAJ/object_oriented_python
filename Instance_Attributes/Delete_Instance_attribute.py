class Dog:
 
    def __init__(self, name):
       self.name = name

dog = Dog("Nora")
print(dog.name)

del dog.name
print(dog.name)
