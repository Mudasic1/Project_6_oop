class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute
    
    @property
    def price(self):
        """Getter method for the price property."""
        return self._price
    
    @price.setter
    def price(self, value):
        """Setter method for the price property."""
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        """Deleter method for the price property."""
        print(f"Deleting price for {self.name}")
        self._price = 0
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percent):
        super().__init__(name, price)
        self.discount_percent = discount_percent
    
    @property
    def discounted_price(self):
        """Get the price after applying the discount."""
        discount = self.price * (self.discount_percent / 100)
        return self.price - discount
    
    def __str__(self):
        return f"{self.name}: ${self.price:.2f} (Discount: {self.discount_percent}%, Final: ${self.discounted_price:.2f})"

# Test the property decorators
if __name__ == "__main__":
    # Create a product
    laptop = Product("Laptop", 1200)
    
    # Use the getter
    print(f"Original price: ${laptop.price}")
    
    # Use the setter
    laptop.price = 1300
    print(f"Updated price: ${laptop.price}")
    
    # Try to set an invalid price
    try:
        laptop.price = -100
    except ValueError as e:
        print(f"Error: {e}")
    
    # Create a discounted product
    phone = DiscountedProduct("Smartphone", 800, 15)
    print(phone)
    
    # Change the price and discount
    phone.price = 850
    phone.discount_percent = 20
    print(phone)
    
    # Use the deleter
    print("\nDeleting price...")
    del laptop.price
    print(f"Price after deletion: ${laptop.price}")
    
    # Show that property works like a regular attribute in many cases
    products = [
        Product("Tablet", 500),
        Product("Headphones", 150),
        DiscountedProduct("Monitor", 300, 10)
    ]
    
    # Sort products by price
    sorted_products = sorted(products, key=lambda p: p.price)
    
    print("\nProducts sorted by price:")
    for product in sorted_products:
        print(product) 