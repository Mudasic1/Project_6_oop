class A:
    def show(self):
        return "This is class A's show method"
    
    def info(self):
        return "Class A info"

class B(A):
    def show(self):
        return "This is class B's show method"
    
    def display_b(self):
        return "Class B specific method"

class C(A):
    def show(self):
        return "This is class C's show method"
    
    def display_c(self):
        return "Class C specific method"

class D(B, C):
    def display_d(self):
        return "Class D specific method"
    
    # Uncomment the following to override show() in class D
    # def show(self):
    #     return "This is class D's show method"

# Test the Method Resolution Order
if __name__ == "__main__":
    # Create instances of each class
    a = A()
    b = B()
    c = C()
    d = D()
    
    # Call show() method on each instance
    print("Calling show() on each instance:")
    print(f"A.show(): {a.show()}")
    print(f"B.show(): {b.show()}")
    print(f"C.show(): {c.show()}")
    print(f"D.show(): {d.show()}")
    
    # Check Method Resolution Order for class D
    print("\nMethod Resolution Order for class D:")
    print(D.__mro__)
    
    # Explain the MRO result
    print("\nExplanation of MRO for class D:")
    print("D.__mro__ shows the order in which Python searches for methods when called on a D instance.")
    print("The search order is: D -> B -> C -> A -> object")
    print("This is why d.show() returns B's implementation, not C's.")
    
    # Call specific methods from each parent class
    print("\nCalling specific methods:")
    print(f"d.display_b(): {d.display_b()}")  # From B
    print(f"d.display_c(): {d.display_c()}")  # From C
    print(f"d.display_d(): {d.display_d()}")  # From D
    print(f"d.info(): {d.info()}")            # From A (inherited through both B and C)
    
    # Test super() in relation to MRO
    print("\nDemonstrating super() with MRO:")
    
    class E(D):
        def show(self):
            result = super().show()  # This will call B.show() based on MRO
            return f"E.show() calling super: {result}"
    
    e = E()
    print(f"E.show(): {e.show()}")
    print("\nMethod Resolution Order for class E:")
    print(E.__mro__) 