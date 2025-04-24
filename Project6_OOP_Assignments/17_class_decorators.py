def add_greeting(cls):
    """
    A class decorator that adds a greet() method to the class.
    """
    # Define the method to add to the class
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the method to the class
    cls.greet = greet
    
    # Return the modified class
    return cls

# Apply the decorator to a class
@add_greeting
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Another class with the decorator
@add_greeting
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def job_info(self):
        return f"{self.name} works as a {self.position}."

# A class without the decorator
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def study_info(self):
        return f"{self.name} is in grade {self.grade}."

# Test the class decorator
if __name__ == "__main__":
    # Create a Person instance
    person = Person("John", 30)
    
    # Use the original methods
    print(person.introduce())
    
    # Use the method added by the decorator
    print(person.greet())
    
    # Create an Employee instance
    employee = Employee("Alice", "Software Engineer")
    print(employee.job_info())
    print(employee.greet())  # This method was added by the decorator
    
    # Create a Student instance (without the decorator)
    student = Student("Bob", 10)
    print(student.study_info())
    
    # Try to call greet() on Student (should fail)
    try:
        print(student.greet())
    except AttributeError as e:
        print(f"Error: {e}")
    
    # Add the decorator manually to the Student class
    print("\nAdding the decorator to Student class manually:")
    Student = add_greeting(Student)
    
    # Create a new student
    student2 = Student("Emily", 11)
    print(student2.study_info())
    print(student2.greet())  # Now this should work 