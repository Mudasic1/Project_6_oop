class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.is_sitting = False
    
    # Instance method
    def bark(self):
        return f"{self.name} says: Woof! Woof!"
    
    # Instance method with parameters
    def eat(self, food):
        return f"{self.name} is eating {food}."
    
    # Instance method that changes instance variables
    def sit(self):
        self.is_sitting = True
        return f"{self.name} is now sitting."
    
    # Instance method that changes instance variables
    def stand(self):
        self.is_sitting = False
        return f"{self.name} is now standing."
    
    # Instance method that uses instance variables
    def description(self):
        sitting_status = "sitting" if self.is_sitting else "standing"
        return f"{self.name} is a {self.breed} and is currently {sitting_status}."

# Test the Dog class
if __name__ == "__main__":
    # Create dog instances
    fido = Dog("Fido", "Labrador")
    spot = Dog("Spot", "Dalmatian")
    
    # Call instance methods on fido
    print(fido.bark())
    print(fido.eat("dog food"))
    print(fido.description())
    print(fido.sit())
    print(fido.description())
    print(fido.stand())
    print(fido.description())
    
    print("\n-------------\n")
    
    # Call instance methods on spot
    print(spot.bark())
    print(spot.eat("a bone"))
    print(spot.description())
    print(spot.sit())
    print(spot.description()) 