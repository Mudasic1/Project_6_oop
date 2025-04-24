class Employee:
    def __init__(self, name, employee_id, role):
        self.name = name
        self.employee_id = employee_id
        self.role = role
        self.department = None  # Will be set when added to a department
    
    def display_info(self):
        dept_info = f"Department: {self.department.name}" if self.department else "Not assigned to any department"
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Role: {self.role}, {dept_info}"
    
    def __str__(self):
        return f"{self.name} ({self.role})"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Aggregation: Department "has" Employees
    
    def add_employee(self, employee):
        # We store a reference to the employee
        self.employees.append(employee)
        # Update the employee's department reference
        employee.department = self
        print(f"Added {employee.name} to {self.name} department")
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            employee.department = None
            print(f"Removed {employee.name} from {self.name} department")
        else:
            print(f"{employee.name} is not in {self.name} department")
    
    def list_employees(self):
        if not self.employees:
            return f"No employees in {self.name} department"
        
        result = f"Employees in {self.name} department:"
        for employee in self.employees:
            result += f"\n- {employee}"
        return result
    
    def get_employee_count(self):
        return len(self.employees)

# Test the aggregation relationship
if __name__ == "__main__":
    # Create Employee objects (these exist independently)
    john = Employee("John Smith", "E001", "Developer")
    mary = Employee("Mary Johnson", "E002", "Manager")
    bob = Employee("Bob Wilson", "E003", "Designer")
    alice = Employee("Alice Brown", "E004", "Developer")
    
    # Create Department objects
    engineering = Department("Engineering")
    design = Department("Design")
    
    # Display initial info
    print(john.display_info())
    print(bob.display_info())
    
    # Add employees to departments
    engineering.add_employee(john)
    engineering.add_employee(mary)
    design.add_employee(bob)
    
    # Display updated info
    print("\nDepartment Info:")
    print(engineering.list_employees())
    print(design.list_employees())
    
    # Display employee info again (now with department)
    print("\nUpdated Employee Info:")
    print(john.display_info())
    print(bob.display_info())
    
    # Move an employee between departments
    print("\nMoving Bob to Engineering:")
    design.remove_employee(bob)
    engineering.add_employee(bob)
    
    # Display final department assignments
    print("\nFinal Department Info:")
    print(f"Engineering department has {engineering.get_employee_count()} employees")
    print(engineering.list_employees())
    print(f"Design department has {design.get_employee_count()} employees")
    print(design.list_employees())
    
    # Demonstrate that employees can exist without being in a department
    print("\nCreating a new employee not in any department:")
    print(alice.display_info()) 