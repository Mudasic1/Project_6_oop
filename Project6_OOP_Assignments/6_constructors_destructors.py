class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Constructor: Logger object '{self.name}' created")
    
    def log(self, message):
        print(f"Log [{self.name}]: {message}")
    
    def __del__(self):
        print(f"Destructor: Logger object '{self.name}' destroyed")

# Test the Logger class
if __name__ == "__main__":
    print("Creating first logger...")
    logger1 = Logger("MainLogger")
    logger1.log("This is a test message")
    
    print("\nCreating second logger...")
    logger2 = Logger("BackupLogger")
    logger2.log("System running smoothly")
    
    print("\nDeleting first logger...")
    del logger1
    
    print("\nProgram continues...")
    logger2.log("Still logging")
    
    print("\nEnd of program (second logger will be destroyed automatically)")
    # logger2 will be automatically destroyed when the program ends 