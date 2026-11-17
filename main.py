#Main user interface for the Book Management System.
from manager import BookManager
from validation import BookValidator

class BookApp:
    def __init__(self) -> None:
        self.manager = BookManager()

    #Display the main menu.
    def show_menu(self):
        print("=" * 40)
        print("        BOOK MANAGEMENT SYSTEM")
        print("=" * 40)
        print("1. Add a new Book")
        print("2. Show all Books")
        print("3. Search for a Book")
        print("4. EXIT")
        print("=" * 40)

    #Validate user input and retry is necessary.
    def get_valid_input(self, prompt, validator):
        while True:
            try:
                value = input(prompt)
                return validator(value)
            except ValueError as e:
                print(e)
                
    #Get book information from the user.
    def add_book_menu(self):
        print("\nAdd a new book")
        print("-" * 40)

        title = self.get_valid_input("Enter book title: ", BookValidator.validate_text)
        author = self.get_valid_input("Enter author: ", BookValidator.validate_text)
        year = self.get_valid_input("Enter publication year: ", BookValidator.validate_year)

        print("\nSelect book type:")
        print("1. Printed Book")
        print("2. EBook")

        while True:
            book_type = input("Enter your choice: ").strip()
            if book_type in ["1", "2"]:
                break
            print("Please select a valid book type.")

        if book_type == "1":
            self.manager.add_book(title, author, year, "printed book")
        elif book_type == "2":
            file_format = self.get_valid_input("Enter format (PDF, EPUB, MOBI, AZW3): ", BookValidator.validate_format)
            self.manager.add_book(title, author, year, "ebook", file_format)

    #Get the book title to search for.
    def search_book_menu(self):
        print("\nSearch for a book")
        print("-" * 40)

        title = self.get_valid_input("Enter book title: ", BookValidator.validate_text)
        self.manager.search_book(title)

    #Run the application and handle user choices.
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.add_book_menu()
            elif choice == "2":
                self.manager.show_all_books()
            elif choice == "3":
                self.search_book_menu()
            elif choice =="4":
                print("Goodbye!")
                break
            else:
                print("Please select a valid option.")

if __name__ == "__main__":
    try:
        app = BookApp()
        app.run()
    except (ValueError, OSError) as e:
        print(e)

    

