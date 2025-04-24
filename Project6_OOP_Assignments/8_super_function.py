class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
    def greet(self):
        print(f"Hello, my name is {self.name}!")

class Teacher(Person):
    def __init__(self, name, age, subject):
        # Call the parent class constructor using super()
        super().__init__(name, age)
        self.subject = subject
    
    # Override the display method
    def display(self):
        # Call the parent class display method using super()
        super().display()
        print(f"Subject: {self.subject}")
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

# Test the Person and Teacher classes
if __name__ == "__main__":
    # Create a Person instance
    print("Creating a Person:")
    person = Person("John", 35)
    person.display()
    person.greet()
    
    print("\nCreating a Teacher:")
    # Create a Teacher instance
    teacher = Teacher("Mrs. Smith", 42, "Mathematics")
    teacher.display()  # This calls the overridden display method
    teacher.greet()    # This calls the inherited greet method
    teacher.teach()    # This calls the Teacher class method 