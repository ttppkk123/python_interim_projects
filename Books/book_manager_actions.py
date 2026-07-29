from constants import OPTION_NAMES, BOOK_TYPE_OPTIONS
from book import PrintedBook, EBook
from validations import input_text, input_int, input_float, input_year

# Display the list of books
def display_books(books):
    print("-" * 30)
    for index, book in enumerate(books, start=1):
        print(f"{index}. {book.display_book_details()}")

# Display the application menu
def display_menu():
    print("\nBook Management Application")
    print("-" * 30)
    for number in OPTION_NAMES:
            print(f"{number}. {OPTION_NAMES[number]}")
    print("-" * 30)

# Choose book type
def choose_book_type():
    print("\nChoose book type:")
    for number in BOOK_TYPE_OPTIONS:
        print(f"{number}. {BOOK_TYPE_OPTIONS[number]}")

    while True:
        choice = input_int("Choose book type: ")
        if choice == 1 or choice == 2:
            return choice
        else:
            print("Invalid option. Please enter valid option.")

# Add new book to the list based on the user's inputs
def add_new_book(manager):
    print("\nAdd New Book")
    print("-" * 30)

    while True:
        try:
            title = input_text("Enter book title: ")
            author = input_text("Enter book author: ")
            year = input_year("Enter publication year: ")
            book_type = choose_book_type()

            if book_type == 1:
                pages = input_int("Enter number of pages: ")
                book = PrintedBook(title, author, year, pages)

            elif book_type == 2:
                file_size = input_float("Enter file size in MB: ")
                book = EBook(title, author, year, file_size)

            manager.add_book(book)

            print("\nBook added successfully!")
            break
        
        except ValueError as error:
            print(error)
            print("Please try again.")

# Search book in the book list based on the title entered by the user
def search_book_by_title(manager):
    print("\nSearch Book By Title")
    print("-" * 30)

    if not manager.has_books():
        print("\nNo books available for search.")
        return

    title = input_text("Enter book title: ")
    results = manager.search_by_title(title)

    if not results:
        print("\nNo book found with that title.")
    else:
        print("\nSearch Results")
        display_books(results)

# Search book in the book list based on the author entered by the user
def search_book_by_author(manager):
    print("\nSearch Book By Author")
    print("-" * 30)

    if not manager.has_books():
        print("\nNo books available for search.")
        return

    author = input_text("Enter book's author: ")
    results = manager.search_by_author(author)

    if not results:
        print("\nNo book found written by that author.")
    else:
        print("\nSearch Results")
        display_books(results)

# Search book in the book list based on the publication year entered by the user
def search_book_by_year(manager):
    print("\nSearch Book By Publication Year")
    print("-" * 30)

    if not manager.has_books():
        print("\nNo books available for search.")
        return

    year = input_year("Enter publication year: ")
    results = manager.search_by_year(year)

    if not results:
        print("\nNo book found with that publication year.")
    else:
        print("\nSearch Results")
        display_books(results)

# Update book details
def update_book_details(manager):
    print("\nUpdate Book Details")
    print("-" * 30)    

    if not manager.has_books():
        print("\nNo books available for update.")
        return

    title = input_text("Enter title of the book to update: ")
    book = manager.find_book_by_title(title)
    if not book:
        print("\nNo book found with that title.")
        return
    else:
        print("\nBook Found - What would you like to update?")
        print("1. Title")
        print("2. Author")
        print("3. Publication Year")

        if isinstance(book, PrintedBook):
            print("4. Number of Pages")
        elif isinstance(book, EBook):
            print("4. File Size")

        print("0. Cancel")

        choice = input_int("Choose an option: ")

        while True:
            try:
                if choice == 1:
                    book.title = input_text("Enter new title: ")

                elif choice == 2:
                    book.author = input_text("Enter new author: ")

                elif choice == 3:
                    book.year = input_year("Enter new publication year: ")
                    
                elif choice == 4:
                    if isinstance(book, PrintedBook):
                        book.pages = input_int("Enter new number of pages: ")
                        
                    elif isinstance(book, EBook):
                        book.file_size = input_float("Enter new file size in MB: ")
                        
                elif choice == 0:
                    print("Update cancelled.")
                    return

                else:
                    print("Invalid option.")
                    return

                print("\nBook updated successfully!")
                print(book.display_book_details())
                break

            except ValueError as error:
                print(error)
                print("Please try again.")

# Filter books by type
def filter_books_by_type(manager):
    print("\nFilter Books By Type")
    print("-" * 30)

    if not manager.has_books():
        print("\nNo books available to filter.")
        return

    for number in BOOK_TYPE_OPTIONS:
        print(f"{number}. {BOOK_TYPE_OPTIONS[number]}")
    print("0. Cancel")

    book_type = input_int("Choose book type: ")

    if book_type == 0:
        print("Filter cancelled.")
        return

    if book_type != 1 and book_type != 2:
        print("Invalid option. Please enter valid option.")
        return

    results = manager.filter_books_by_type(book_type)

    if not results:
        print("\nNo books found for that type.")
    else:
        print("\nFiltered Books")
        display_books(results)

# Delete book
def delete_book(manager):
    print("\nDelete book by title")
    print("-" * 30)

    if not manager.has_books():
        print("\nNo books available for search.")
        return
    
    title = input_text("Enter book title to delete: ")
    deleted_book = manager.delete_book(title)
    
    if not deleted_book:
        print("\nNo book found with that title.")
    else:
        print("\nBook deleted successfully")
        print(f"Deleted: {deleted_book.display_book_details()}")
 