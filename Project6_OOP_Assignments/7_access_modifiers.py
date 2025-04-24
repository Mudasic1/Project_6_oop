class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # Public variable
        self._salary = salary      # Protected variable (convention)
        self.__ssn = ssn           # Private variable
    
    def display_public(self):
        print(f"Public - Name: {self.name}")
    
    def display_protected(self):
        print(f"Protected - Salary: {self._salary}")
    
    def display_private(self):
        print(f"Private - SSN: {self.__ssn}")
    
    def display_all(self):
        self.display_public()
        self.display_protected()
        self.display_private()

# Test the Employee class
if __name__ == "__main__":
    # Create an employee
    emp = Employee("John Doe", 75000, "123-45-6789")
    
    print("Accessing variables from inside class methods:")
    emp.display_all()
    
    print("\nAccessing variables from outside the class:")
    
    # Access public variable
    print(f"Public - Name: {emp.name}")  # Works fine
    
    # Try to access protected variable
    try:
        print(f"Protected - Salary: {emp._salary}")  # Works but not recommended
        print("Note: Protected variables can be accessed, but it's not recommended")
    except Exception as e:
        print(f"Error accessing protected variable: {e}")
    
    # Try to access private variable
    try:
        print(f"Private - SSN: {emp.__ssn}")  # Will cause AttributeError
    except Exception as e:
        print(f"Error accessing private variable: {e}")
    
    # Note: Private variables can still be accessed using name mangling
    try:
        print(f"Private (via name mangling) - SSN: {emp._Employee__ssn}")
        print("Note: Private variables can be accessed through name mangling (_Employee__ssn)")
    except Exception as e:
        print(f"Error accessing private variable via name mangling: {e}") 