class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine started.")

# Create an object of the Car class
my_car = Car("Toyota", "Camry", 2020)

# Access attributes of the object
print("Make:", my_car.make)
print("Model:", my_car.model)
print("Year:", my_car.year)

# Call a method of the object
my_car.start_engine()
