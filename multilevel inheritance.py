class Animal:
    def eat(self):
        print("Animal is eating")

class Mammal:
    def walk(self):
        print("Animal is walking")

class Dog(Animal, Mammal):  # Dog inherits from both Animal and Mammal
    def bark(self):
        print("Dog is barking")

# Creating a Dog object
dog = Dog()
dog.eat()   # Inherited from Animal
dog.walk()  # Inherited from Mammal
dog.bark()  # Defined in Dog
