class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        """
        Makes the object callable like a function.
        When called, it multiplies the input by the factor.
        """
        return x * self.factor
    
    def __str__(self):
        return f"Multiplier with factor {self.factor}"

class Adder:
    def __init__(self, value):
        self.value = value
    
    # No __call__ method

# Test the callable class
if __name__ == "__main__":
    # Create Multiplier instances
    double = Multiplier(2)
    triple = Multiplier(3)
    
    # Check if the object is callable
    print(f"Is double callable? {callable(double)}")
    
    # Use the object like a function
    print(f"Double 5: {double(5)}")
    print(f"Double 10: {double(10)}")
    
    print(f"Triple 7: {triple(7)}")
    
    # Create a list of multipliers
    multipliers = [Multiplier(i) for i in range(1, 6)]
    
    # Apply each multiplier to a number
    number = 8
    print(f"\nApplying different multipliers to {number}:")
    for multiplier in multipliers:
        print(f"{multiplier}: {multiplier(number)}")
    
    # Create an adder (not callable)
    adder = Adder(5)
    
    # Check if the adder is callable
    print(f"\nIs adder callable? {callable(adder)}")
    
    # Try to call the adder
    try:
        result = adder(10)
        print(f"Result: {result}")
    except TypeError as e:
        print(f"Error: {e}")
    
    # Examples of built-in callables
    print("\nExamples of built-in callables:")
    print(f"Is len callable? {callable(len)}")
    print(f"Is str callable? {callable(str)}")
    print(f"Is print callable? {callable(print)}")
    
    # Creating a lambda function
    square = lambda x: x * x
    print(f"Is lambda (square) callable? {callable(square)}")
    print(f"Square of 9: {square(9)}") 