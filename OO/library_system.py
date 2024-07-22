class Book:
    def __init__(self, title, author, isbn, available_copies=0):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available_copies = available_copies
        
        
    def get_title(self):
        return self._title
        
        
    def set_title(self, title):
        self._title = title
        
        
    def get_author(self):
        return self._author
    
    
    def set_author(self, author):
        self._author = author
        
        
    def get_isbn(self):
        return self._isbn
    
    
    def set_isbn(self, isbn):
        self._isbn = isbn
        
        
    def get_available_copies(self):
        return self._available_copies
    
    
    def set_available_copies(self, available_copies):
        self._available_copies = available_copies
        
        
    def borrow(self):
        if self._available_copies > 0:
            self._available_copies -= 1
            return True
        else:
            return False
    
    
    def return_book(self):
        self._available_copies += 1
        
        
class Member:
    def __init__(self, name, member_id):
        self._name = name
        self._member_id = member_id
        self._borrowed_books = []
        
    
    def get_name(self):
        return self._name
    
    
    def set_name(self, name):
        self._name = name
        
        
    def get_member_id(self):
        return self._member_id
    
    
    def set_member_id(self, member_id):
        self._member_id = member_id
        
    
    def get_borrowed_books(self):
        return self._borrowed_books
    
    
    def borrow_book(self, book):
        return self._borrowed_books.append(book)
    
    
    def return_book(self, book):
        return self._borrowed_books.remove(book)
    
    
class Library:
    def __init__(self):
        self._books = []
        self._members = []
        
        
    def add_book(self, book):
        self._books.append(book)
        
        
    def register_member(self, member):
        self._members.append(member)
        
        
    def borrow_book(self, member_id, book_isbn):
        member = next((m for m in self._members if m.get_member_id() == member_id), None)
        book = next((b for b in self._books if b.get_isbn() == book_isbn), None)
         
        if member and book and book.borrow():
            member.borrow_book(book)
            return f'{member.get_name()} successfully borrowed {book.get_title()}'
         
        return 'Unable to borrow book.'
     
     
    def return_book(self, member_id,  book_isbn):
        member = next((m for m in self._members if m.get_member_id() == member_id), None)
        book = next((b for b in self._books if b.get_isbn() == book_isbn), None)
        
        if member and book and book in member.get_borrowed_books():
            member.return_book(book)
            book.return_book()
            return f'{member.get_name()} successfully returned {book.get_title()}'
        return 'Book returning failed.'
        
        
# Example usage:
if __name__ == "__main__":
    # Create some books
    book1 = Book("1984", "George Orwell", "1234567890", 3)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321", 2)

    # Create some members
    member1 = Member("Alice", "M001")
    member2 = Member("Bob", "M002")

    # Create a library and add books and members
    my_library = Library()
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.register_member(member1)
    my_library.register_member(member2)
    
    # Borrow and return books
    print(my_library.borrow_book("M001", "1234567890"))