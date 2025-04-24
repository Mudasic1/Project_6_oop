class Counter:
    # Class variable to keep track of the count
    count = 0
    
    def __init__(self):
        # Increment count when an object is created
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")
    
    @classmethod
    def reset_count(cls):
        cls.count = 0
        print("Counter has been reset to 0")

# Test the Counter class
if __name__ == "__main__":
    counter1 = Counter()
    counter2 = Counter()
    counter3 = Counter()
    
    Counter.display_count()  # Should display 3
    
    counter4 = Counter()
    counter5 = Counter()
    
    Counter.display_count()  # Should display 5
    
    Counter.reset_count()
    Counter.display_count()  # Should display 0 