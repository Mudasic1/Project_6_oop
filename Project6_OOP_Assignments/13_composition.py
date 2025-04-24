class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.running = False
    
    def start(self):
        self.running = True
        return f"Engine started. {self.horsepower} HP {self.fuel_type} engine is running."
    
    def stop(self):
        self.running = False
        return "Engine stopped."
    
    def status(self):
        status = "running" if self.running else "not running"
        return f"{self.horsepower} HP {self.fuel_type} engine is {status}."
    
    def accelerate(self):
        if self.running:
            return "Vroom! Engine is accelerating."
        else:
            return "Can't accelerate. Engine is not running."

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        # Composition: Car "has-a" Engine
        self.engine = engine
        self.speed = 0
    
    def start_car(self):
        result = self.engine.start()
        return f"Car starting: {result}"
    
    def stop_car(self):
        result = self.engine.stop()
        self.speed = 0
        return f"Car stopping: {result}"
    
    def accelerate(self, speed_increase):
        if self.engine.running:
            engine_response = self.engine.accelerate()
            self.speed += speed_increase
            return f"{engine_response} Car speed increased to {self.speed} mph."
        else:
            return "Car can't accelerate. Engine is not running."
    
    def get_car_details(self):
        return f"{self.make} {self.model} with {self.engine.status()}"

# Test the composition relationship
if __name__ == "__main__":
    # Create an Engine object
    v8_engine = Engine(300, "gasoline")
    
    # Create a Car object with the Engine
    my_car = Car("Toyota", "Camry", v8_engine)
    
    # Access Engine methods through Car
    print(my_car.get_car_details())
    print(my_car.start_car())
    print(my_car.get_car_details())
    print(my_car.accelerate(20))
    print(my_car.accelerate(30))
    print(my_car.stop_car())
    print(my_car.get_car_details())
    
    # Create another Engine and Car
    print("\nCreating another car with a different engine:")
    electric_engine = Engine(450, "electric")
    electric_car = Car("Tesla", "Model S", electric_engine)
    
    print(electric_car.get_car_details())
    print(electric_car.start_car())
    print(electric_car.accelerate(50))
    print(electric_car.get_car_details()) 