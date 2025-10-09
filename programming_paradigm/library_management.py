class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_checked_out = False
        
    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
    
    def is_available(self):
        return not self.is_checked_out
    
    def __str__(self):
        status = "checked out" if self.is_checked_out else "available"
        return f"{self.title} by {self.author}"


class Library:
    # def __init__(self):
    #     self._books = []

    # def add_book(self,title,author):
    #     book = Book(title,author)
    #     self._books.append(book)
    #     return book
    # def check_out_book(self,title):
    #     for book in self._books:
    #         if book.title == title and not book._is_checked_out:
    #             book._is_checked_out = True
    #             return f"Checked out: {book}"
    #     return "Book not available"
    # def return_book(self,title):
        
    #    for book in self._books:
    #         if book.title == title and book._is_checked_out:
    #             book._is_checked_out = False
    #             return f"Returned: {book}"
    #         return f"Invalid return"
    # def list_available_books(self):
    #     available_books = [book for book in self._books if not book._is_checked_out]
    #     if not available_books:
    #         return "No books available"
    #     return "\n".join(str(book) for book in available_books)
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Add a Book object to the library"""
        if isinstance(book, Book):
            self._books.append(book)
            return f"Added: {book}"
        return "Invalid book object"
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    return f"Checked out: {book}"
        return "Book not available"
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    return f"Returned: {book}"
        return "Invalid return"
    
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available")
            return
        for book in available_books:
            print(str(book))