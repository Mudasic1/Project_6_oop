class Bank:
    # Class variable
    bank_name = "Default Bank"
    
    def __init__(self, branch_name):
        self.branch_name = branch_name
    
    def display_details(self):
        print(f"Bank Name: {Bank.bank_name}")
        print(f"Branch Name: {self.branch_name}")
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name changed to {cls.bank_name}")

# Test the Bank class
if __name__ == "__main__":
    # Create instances of Bank
    branch1 = Bank("Downtown")
    branch2 = Bank("Uptown")
    
    # Display initial details
    print("Initial Bank Details:")
    branch1.display_details()
    branch2.display_details()
    
    # Change the bank name using class method
    Bank.change_bank_name("City National Bank")
    
    # Verify that the change affects all instances
    print("\nUpdated Bank Details:")
    branch1.display_details()
    branch2.display_details()
    
    # Create a new instance
    branch3 = Bank("Suburb")
    
    # Verify that the new instance also has the updated bank name
    print("\nNew Branch Details:")
    branch3.display_details() 