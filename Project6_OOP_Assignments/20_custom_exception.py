class InvalidAgeError(Exception):
    """Exception raised when an age is below the minimum allowed."""
    
    def __init__(self, age, min_age, message=None):
        self.age = age
        self.min_age = min_age
        if message is None:
            message = f"Age {age} is below the minimum age of {min_age}"
        super().__init__(message)

class AgeRangeError(InvalidAgeError):
    """Exception raised when an age is outside an acceptable range."""
    
    def __init__(self, age, min_age, max_age):
        self.max_age = max_age
        message = f"Age {age} is outside the acceptable range of {min_age} to {max_age}"
        super().__init__(age, min_age, message)

def check_age(age, min_age=18):
    """Check if the age is at least the minimum age."""
    if age < min_age:
        raise InvalidAgeError(age, min_age)
    return True

def check_age_range(age, min_age=18, max_age=65):
    """Check if the age is within the specified range."""
    if age < min_age or age > max_age:
        raise AgeRangeError(age, min_age, max_age)
    return True

# Test the custom exceptions
if __name__ == "__main__":
    # Test with valid age
    try:
        check_age(20)
        print("Age 20 is valid")
    except InvalidAgeError as e:
        print(f"Error: {e}")
    
    # Test with invalid age
    try:
        check_age(16)
        print("Age 16 is valid")
    except InvalidAgeError as e:
        print(f"Error: {e}")
    
    # Test with custom min_age
    try:
        check_age(19, min_age=21)
        print("Age 19 is valid for min_age=21")
    except InvalidAgeError as e:
        print(f"Error: {e}")
    
    # Test age range check
    print("\nTesting age range checks:")
    
    # Test with age in range
    try:
        check_age_range(30, min_age=18, max_age=65)
        print("Age 30 is within range of 18-65")
    except AgeRangeError as e:
        print(f"Error: {e}")
    
    # Test with age below range
    try:
        check_age_range(15, min_age=18, max_age=65)
        print("Age 15 is within range of 18-65")
    except AgeRangeError as e:
        print(f"Error: {e}")
    
    # Test with age above range
    try:
        check_age_range(70, min_age=18, max_age=65)
        print("Age 70 is within range of 18-65")
    except AgeRangeError as e:
        print(f"Error: {e}")
    
    # Demonstrate catching parent exception
    print("\nDemonstrating exception hierarchy:")
    try:
        check_age_range(15, min_age=18, max_age=65)
        print("Age 15 is within range of 18-65")
    except InvalidAgeError as e:  # This will catch AgeRangeError too
        print(f"Caught using parent exception class: {e}") 