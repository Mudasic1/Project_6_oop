import time
import functools

def log_function_call(func):
    @functools.wraps(func)  # Preserves the original function's metadata
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' is being called")
        # Get the start time
        start_time = time.time()
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Get the end time
        end_time = time.time()
        
        # Print execution time
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")
        
        return result
    return wrapper

# Apply the decorator to a function
@log_function_call
def say_hello(name):
    time.sleep(0.5)  # Simulate some work
    return f"Hello, {name}!"

@log_function_call
def calculate_sum(a, b):
    time.sleep(0.3)  # Simulate some work
    return a + b

# Another way to apply a decorator (without using @)
def calculate_product(a, b):
    time.sleep(0.2)  # Simulate some work
    return a * b

# Manually decorate the function
decorated_calculate_product = log_function_call(calculate_product)

# Test the decorated functions
if __name__ == "__main__":
    # Call the decorated function
    result = say_hello("Alice")
    print(f"Result: {result}")
    
    print("\n-------------------\n")
    
    # Call another decorated function
    result = calculate_sum(5, 3)
    print(f"Result: {result}")
    
    print("\n-------------------\n")
    
    # Call the manually decorated function
    result = decorated_calculate_product(4, 7)
    print(f"Result: {result}")
    
    # Demonstrate that the original function is unchanged
    print("\n-------------------\n")
    print("Calling the original calculate_product function:")
    result = calculate_product(4, 7)
    print(f"Result: {result} (called without logging)")
    
    # Show that functools.wraps preserved the function's metadata
    print("\n-------------------\n")
    print(f"Original function name: {say_hello.__name__}")
    print(f"Original function docstring: {say_hello.__doc__}") 