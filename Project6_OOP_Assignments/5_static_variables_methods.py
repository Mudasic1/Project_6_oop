class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

# Test the MathUtils class
if __name__ == "__main__":
    # No need to create an instance, can call static methods directly from the class
    print(f"5 + 3 = {MathUtils.add(5, 3)}")
    print(f"10 - 4 = {MathUtils.subtract(10, 4)}")
    print(f"7 * 6 = {MathUtils.multiply(7, 6)}")
    print(f"15 / 5 = {MathUtils.divide(15, 5)}")
    print(f"10 / 0 = {MathUtils.divide(10, 0)}")
    
    # Can also call static methods from an instance (not recommended, but possible)
    math_instance = MathUtils()
    print(f"Using instance: 8 + 2 = {math_instance.add(8, 2)}") 