class Dog:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

# Create two objects of the Dog class
dog1 = Dog("Labrador", "Max", 3)
dog2 = Dog("Golden Retriever", "Buddy", 5)

# Access the attributes of each object
print("Dog 1:", dog1.breed, dog1.name, dog1.age)
print("Dog 2:", dog2.breed, dog2.name, dog2.age)
