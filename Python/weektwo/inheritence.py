class Animal:
    def __init__(self, species):
        self.species = species

class Dog(Animal):
    def __init__(self, breed, name, age):
        Animal.__init__(self, "Canine")
        self.breed = breed
        self.name = name
        self.age = age

# Create an object of the Dog class
dog = Dog("Labrador", "Max", 3)

# Access the species attribute from the parent Animal class
print("Species:", dog.species)
