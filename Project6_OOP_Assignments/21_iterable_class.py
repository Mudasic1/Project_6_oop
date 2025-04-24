class Countdown:
    def __init__(self, start):
        """Initialize the countdown with a starting number."""
        if not isinstance(start, int) or start < 0:
            raise ValueError("Start value must be a non-negative integer")
        self.start = start
    
    def __iter__(self):
        """Return an iterator object (self)."""
        # Create a new counter starting from the initial value
        self.current = self.start
        return self
    
    def __next__(self):
        """Return the next value in the countdown sequence."""
        if self.current < 0:
            # Stop iteration when we go below 0
            raise StopIteration
        
        # Store the current value
        value = self.current
        # Decrement for the next iteration
        self.current -= 1
        # Return the current value
        return value

class RangeIterator:
    """A custom implementation of range functionality."""
    
    def __init__(self, start, stop=None, step=1):
        """Initialize with start, stop, and step values."""
        if stop is None:
            # If only one argument is provided, it's the stop value
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        
        self.step = step
        
        if self.step == 0:
            raise ValueError("Step cannot be zero")
    
    def __iter__(self):
        """Return an iterator object."""
        self.current = self.start
        return self
    
    def __next__(self):
        """Return the next value in the range."""
        if (self.step > 0 and self.current >= self.stop) or \
           (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value

# Test the iterable class
if __name__ == "__main__":
    # Create a Countdown object
    countdown = Countdown(5)
    
    print("Testing Countdown iterator:")
    # Iterate through the countdown using a for loop
    for num in countdown:
        print(num, end=" ")
    print()  # newline
    
    # Create another countdown and convert to a list
    countdown2 = Countdown(3)
    countdown_list = list(countdown2)
    print(f"Countdown as list: {countdown_list}")
    
    # Try an invalid input
    try:
        invalid_countdown = Countdown(-5)
    except ValueError as e:
        print(f"Error: {e}")
    
    # Use multiple iterators on the same object
    print("\nMultiple iterations of the same Countdown object:")
    countdown3 = Countdown(2)
    
    print("First iteration:", end=" ")
    for num in countdown3:
        print(num, end=" ")
    print()
    
    print("Second iteration:", end=" ")
    for num in countdown3:
        print(num, end=" ")
    print()
    
    # Test the RangeIterator
    print("\nTesting RangeIterator:")
    range_iter = RangeIterator(0, 10, 2)
    print("Range(0, 10, 2):", end=" ")
    for num in range_iter:
        print(num, end=" ")
    print()
    
    # Use negative step
    range_iter2 = RangeIterator(10, 0, -1)
    print("Range(10, 0, -1):", end=" ")
    for num in range_iter2:
        print(num, end=" ")
    print() 