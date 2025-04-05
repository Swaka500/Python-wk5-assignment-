# Python OOP Assignment - Device Class Hierarchy

# Base class representing a general device
class Device:
    def __init__(self, brand, model):
        # Private attributes (encapsulation)
        self.__brand = brand
        self.__model = model

    # Getter methods to access private attributes
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    # Method for powering on the device common to all devices
    def power_on(self):
        print(f"{self.__brand} {self.__model} is powering on...")

    # Method to power off the device common to all devices
    def power_off(self):
        print(f"{self.__brand} {self.__model} is powering off...")

# Derived class representing a Smartphone, inheriting from Device
class Smartphone(Device):
    def __init__(self, brand, model, storage, operating_system):
        # Call the constructor of the parent (Device) class
        super().__init__(brand, model)
        self.__storage = storage
        self.__operating_system = operating_system

    # Method to display smartphone details (overriding the base class method)
    def display_details(self):
        print(f"Brand: {self.get_brand()}")
        print(f"Model: {self.get_model()}")
        print(f"Storage: {self.__storage}GB")
        print(f"Operating System: {self.__operating_system}")

    # Overridden method to make a call (polymorphism)
    def power_on(self):
        print(f"{self.get_brand()} {self.get_model()} with {self.__operating_system} is booting up...")

    # Method to make a call
    def make_call(self, phone_number):
        print(f"Calling {phone_number}...")

    # Method to send a message
    def send_message(self, phone_number, message):
        print(f"Sending message to {phone_number}: {message}")

# Object of the Smartphone class
my_phone = Smartphone("Apple", "Iphone", 128, "iOS")

# Calling methods on the object
my_phone.display_details()
my_phone.make_call("1234567890")
my_phone.send_message("1234567890", "Hey, greetings?")
my_phone.power_on()

# Another object of the Smartphone class
another_phone = Smartphone("Samsung", "Galaxy S21", 256, "Android")
another_phone.display_details()
another_phone.power_on()

# Polymorphism Challenge assignment - Animal/Vehicle

# Base class for animal/vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Car class inherits from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class inherits from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class inherits from Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Function to demonstrate polymorphism
def demonstrate_movement(vehicle):
    vehicle.move()

# Instances of different vehicles
car = Car()
plane = Plane()
boat = Boat()

# Demonstrating polymorphism
demonstrate_movement(car)   # Output: Driving 🚗
demonstrate_movement(plane) # Output: Flying ✈️
demonstrate_movement(boat)  # Output: Sailing 🚤

          # THE END #

