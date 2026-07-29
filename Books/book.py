from constants import MIN_PUBLICATION_YEAR, MAX_PUBLICATION_YEAR, BOOK_TYPE_OPTIONS

# Book class
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    # Validating text fields
    @staticmethod
    def validate_text(value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Error: This field cannot be empty.")

        return value.strip()

    # Getter for the title
    @property
    def title(self):
        return self._title

    # Setter for the title
    @title.setter
    def title(self, value):
        self._title = self.validate_text(value)    

    # Getter for the author
    @property
    def author(self):
        return self._author

    # Setter for the author
    @author.setter
    def author(self, value):
        self._author = self.validate_text(value)   

    # Getter for the year
    @property
    def year(self):
        return self._year

    # Setter for the year
    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("Error: Please enter a valid year.")
        
        if value < MIN_PUBLICATION_YEAR or value > MAX_PUBLICATION_YEAR:
            raise ValueError(f"Error: Year must be between {MIN_PUBLICATION_YEAR} and {MAX_PUBLICATION_YEAR}.")
        self._year = value   

    # Return book's details as a formatted string
    def display_book_details(self):
        return f"Title: {self.title} | Author: {self.author} | Year: {self.year}"


# Child class for printed books
class PrintedBook(Book):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.book_type = BOOK_TYPE_OPTIONS[1]
        self.pages = pages

    # Getter for the number of pages
    @property
    def pages(self):
        return self._pages

    # Setter for the number of pages
    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Please input a number of pages.")

        if value <= 0:
            raise ValueError("Number of pages must be greater than 0.")

        self._pages = value

    # Return book's details as a formatted string
    def display_book_details(self):
        return f"{super().display_book_details()} | Type: {self.book_type} | Pages: {self.pages}"


# Child class for electronic books
class EBook(Book):
    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.book_type = BOOK_TYPE_OPTIONS[2]
        self.file_size = file_size

    # Getter for the file size
    @property
    def file_size(self):
        return self._file_size

    # Setter for the file size
    @file_size.setter
    def file_size(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError("Please input a size of the file in MB.")
    
        if value <= 0:
            raise ValueError("File size must be greater than 0.")
    
        self._file_size = float(value)

    # Return book's details as a formatted string
    def display_book_details(self):
        return f"{super().display_book_details()} | Type: {self.book_type} | File size: {self.file_size} MB"