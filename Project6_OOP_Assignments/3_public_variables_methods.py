class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand
        self.is_running = False
    
    # Public method
    def start(self):
        self.is_running = True
        print(f"{self.brand} car has started.")
    
    # Public method
    def stop(self):
        self.is_running = False
        print(f"{self.brand} car has stopped.")

# Test the Car class
if __name__ == "__main__":
    # Create an instance of Car
    my_car = Car("Toyota")
    
    # Access public variable from outside the class
    print(f"Car brand: {my_car.brand}")
    
    # Change public variable from outside the class
    my_car.brand = "Honda"
    print(f"New car brand: {my_car.brand}")
    
    # Call public methods from outside the class
    my_car.start()
    print(f"Is the car running? {my_car.is_running}")
    
    my_car.stop()
    print(f"Is the car running? {my_car.is_running}") 