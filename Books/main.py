from book_manager import BookManager
from validations import input_int
from book_manager_actions import display_menu, add_new_book, search_book_by_title, search_book_by_author, search_book_by_year, filter_books_by_type, update_book_details, delete_book


# Main function

manager = BookManager()
manager.load_books()

while True:
        
    display_menu()

    choice = input_int("Choose an option: ")
    if choice == 1:
        add_new_book(manager)

    elif choice == 2:
        manager.show_books()
            
    elif choice == 3:
        search_book_by_title(manager)

    elif choice == 4:
        search_book_by_author(manager)

    elif choice == 5:
        search_book_by_year(manager)

    elif choice == 6:
        update_book_details(manager)

    elif choice == 7:
        filter_books_by_type(manager)

    elif choice == 8:
        delete_book(manager)
            
    elif choice == 0:
        print("\nThanks for using the application. Goodbye!")
        break

    else:
        print("Invalid option. Please enter a number from 0 to 8.")

