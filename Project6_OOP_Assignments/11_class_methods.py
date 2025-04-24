class Book:
    # Class variable to track total books
    total_books = 0
    
    # Class variable to store all book titles
    book_titles = []
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
        # Increment the total book count when a new book is added
        Book.increment_book_count()
        
        # Add the title to the list of book titles
        Book.book_titles.append(title)
    
    def display_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        print(f"A new book was added. Total books: {cls.total_books}")
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
    @classmethod
    def get_all_titles(cls):
        return cls.book_titles
    
    @classmethod
    def find_longest_book(cls, books):
        if not books:
            return None
        return max(books, key=lambda book: book.pages)

# Test the Book class
if __name__ == "__main__":
    # Create some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 281)
    book3 = Book("1984", "George Orwell", 328)
    
    # Display information about each book
    print(book1.display_info())
    print(book2.display_info())
    print(book3.display_info())
    
    # Use class methods
    print(f"\nTotal books created: {Book.get_total_books()}")
    print(f"All book titles: {Book.get_all_titles()}")
    
    # Find the longest book
    longest_book = Book.find_longest_book([book1, book2, book3])
    print(f"\nLongest book: {longest_book.display_info()}") 