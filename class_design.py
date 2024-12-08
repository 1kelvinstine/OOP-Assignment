# Parent Class: Superhero
class Superhero:
    def __init__(self, name, power, weakness):
        self.name = name               # Public attribute
        self._power = power            # Protected attribute
        self.__weakness = weakness     # Private attribute

    def display_identity(self):
        return f"I am {self.name}, and my power is {self._power}."

    def reveal_weakness(self):
        return f"My weakness is {self.__weakness}."

    def use_power(self):
        return f"{self.name} uses {self._power}!"

# Child Class: FlyingSuperhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, weakness, flight_speed):
        super().__init__(name, power, weakness)
        self.flight_speed = flight_speed  # Unique to FlyingSuperhero

    def use_power(self):
        # Overriding the parent method to include flight ability
        return f"{self.name} flies at {self.flight_speed} km/h while using {self._power}!"

# Child Class: Speedster
class Speedster(Superhero):
    def __init__(self, name, power, weakness, speed):
        super().__init__(name, power, weakness)
        self.speed = speed  # Unique to Speedster

    def use_power(self):
        # Overriding the parent method
        return f"{self.name} sprints at {self.speed} km/h using {self._power}!"

# Example Usage
# Creating a generic superhero
hero1 = Superhero("Shadow", "Invisibility", "Bright light")
print(hero1.display_identity())
# print(hero1.__weakness)  # This would raise an AttributeError due to encapsulation
print(hero1.reveal_weakness())  # Accessing private data via a method

# Creating a FlyingSuperhero
hero2 = FlyingSuperhero("Skyhawk", "Wind Manipulation", "Tight spaces", 500)
print(hero2.display_identity())
print(hero2.use_power())

# Creating a Speedster
hero3 = Speedster("Flashbolt", "Super Speed", "High friction", 1200)
print(hero3.display_identity())
print(hero3.use_power())
