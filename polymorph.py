# Parent Class: Vehicle
class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving on the road! "

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying in the sky! "

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        return f"{self.name} is sailing on the water! "

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        return f"{self.name} is pedaling down the street! "

# Example Usage
vehicles = [
    Car("Sedan"),
    Plane("Jetliner"),
    Boat("Yacht"),
    Bicycle("Mountain Bike")
]

# Loop through the vehicles and call their move() method
for vehicle in vehicles:
    print(vehicle.move())
