class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def celsius_to_kelvin(celsius):
        """Convert Celsius to Kelvin."""
        return celsius + 273.15
    
    @staticmethod
    def kelvin_to_celsius(kelvin):
        """Convert Kelvin to Celsius."""
        return kelvin - 273.15
    
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        """Convert Fahrenheit to Kelvin."""
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(celsius)
    
    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        """Convert Kelvin to Fahrenheit."""
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)

# Test the TemperatureConverter class
if __name__ == "__main__":
    # Test Celsius to Fahrenheit conversion
    celsius = 25
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
    
    # Test Fahrenheit to Celsius conversion
    fahrenheit = 98.6
    celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius:.2f}°C")
    
    # Test Celsius to Kelvin conversion
    celsius = 0
    kelvin = TemperatureConverter.celsius_to_kelvin(celsius)
    print(f"{celsius}°C = {kelvin:.2f}K")
    
    # Test Kelvin to Celsius conversion
    kelvin = 310.15
    celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
    print(f"{kelvin}K = {celsius:.2f}°C")
    
    # Test Fahrenheit to Kelvin conversion
    fahrenheit = 32
    kelvin = TemperatureConverter.fahrenheit_to_kelvin(fahrenheit)
    print(f"{fahrenheit}°F = {kelvin:.2f}K")
    
    # Test Kelvin to Fahrenheit conversion
    kelvin = 373.15
    fahrenheit = TemperatureConverter.kelvin_to_fahrenheit(kelvin)
    print(f"{kelvin}K = {fahrenheit:.2f}°F") 