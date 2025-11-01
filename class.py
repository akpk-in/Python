# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"
    
    def move(self):
        return f"{self.name} is moving"

# Child classes inherit from Animal
class Dog(Animal):
    def speak(self):  # Override parent method
        return f"{self.name} says Woof!"
    
    def fetch(self):  # New method specific to Dog
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    def speak(self):  # Override parent method
        return f"{self.name} says Meow!"
    
    def scratch(self):  # New method specific to Cat
        return f"{self.name} is scratching"

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.speak())      # Buddy says Woof!
print(dog.move())       # Buddy is moving (inherited)
print(dog.fetch())      # Buddy is fetching the ball

print(cat.speak())      # Whiskers says Meow!
print(cat.move())       # Whiskers is moving (inherited)
print(cat.scratch())    # Whiskers is scratching