from book import PrintedBook, EBook
# BookManager class to manage the list of books
class BookManager:

    def __init__(self):
        self.books = []

    # Load sample books
    def load_books(self):
        sample_books = [
            PrintedBook("The Hobbit", "J.R.R. Tolkien", 1937, 310),
            PrintedBook("To Kill a Mockingbird", "Harper Lee", 1960, 281),
            PrintedBook("1984", "George Orwell", 1949, 328),
            PrintedBook("Pride and Prejudice", "Jane Austen", 1813, 432),
            PrintedBook("The Great Gatsby", "F. Scott Fitzgerald", 1925, 180),
            PrintedBook("The Knight in the Panther's Skin", "Shota Rustaveli", 1712, 300),

            EBook("Data Tutashkhia", "Chabua Amirejibi", 1975, 3.8),
            EBook("Kvachi Kvachantiradze", "Mikheil Javakhishvili", 1924, 2.9),
            EBook("Crime and Punishment", "Fyodor Dostoevsky", 1866, 3.6),
            EBook("Anna Karenina", "Leo Tolstoy", 1878, 4.1),
            EBook("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 1967, 3.4)
        ]

        for book in sample_books:
            self.add_book(book)

    # Check if there are books in the list
    def has_books(self):
        return len(self.books) > 0

    # Add book
    def add_book(self, book):
        self.books.append(book)

    # Show book list
    def show_books(self):
        if not self.books:
            print("\nNo books have been added yet.")
            return
        
        print("\nBook List")
        print("-" * 30)
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book.display_book_details()}")

    # Search book by title
    def search_by_title(self, title):
        found_books = []

        for book in self.books:
            if title.lower() in book.title.lower():
                found_books.append(book)

        return found_books

    # Search book by author
    def search_by_author(self, author):
        found_books = []
    
        for book in self.books:
            if author.lower() in book.author.lower():
                found_books.append(book)
    
        return found_books

    # Search book by year
    def search_by_year(self, year):
        found_books = []
        
        for book in self.books:
            if book.year == year:
                found_books.append(book)
        
        return found_books

    # Find book by exact title
    def find_book_by_title(self, title):
        
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

    # Filter books by type
    def filter_books_by_type(self, book_type):
        filtered_books = []

        for book in self.books:
            if book_type == 1 and isinstance(book, PrintedBook):
                filtered_books.append(book)

            elif book_type == 2 and isinstance(book, EBook):
                filtered_books.append(book)

        return filtered_books

    # delete book
    def delete_book(self, title):
        book = self.find_book_by_title(title)

        if book is None:
            return None
        
        self.books.remove(book)
        return book