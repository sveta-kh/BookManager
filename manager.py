#Class for managing the book collection
from book import Book, PrintedBook, EBook
from validation import BookValidator
from storage import BookStorage

class BookManager:
    def __init__(self, filename: str = "books.json") -> None:
        self.storage = BookStorage(filename)
        self.__books: list[Book] = self.storage.load_books()

    # Validate data and add e new book.
    def add_book(self, title: str, author: str, year: int, book_type: str, file_format: str=""):
        try:
            title = BookValidator.validate_text(title)
            author = BookValidator.validate_text(author)
            year = BookValidator.validate_year(year)
            book_type = BookValidator.validate_book_type(book_type)

            book: Book
            if book_type == "printed book":
               book = PrintedBook(title, author, year)

            else:
                file_format = BookValidator.validate_format(file_format)
                book = EBook(title, author, year, file_format)
            
            self.__books.append(book)
            self.storage.save_books(self.__books)
            
            print("Book added successfully.")
        
        except ValueError as e:
            print(e)
        except OSError as e:
            self.__books.pop()
            print(e)

    #Display all books in the collection.
    def show_all_books(self):
        if not self.__books:
            print("The book collection is empty.")

        for book in self.__books:
            print(book.get_info())
            print("-" * 40)

    #Search for a book by its title.
    def search_book(self, title: str):
        try:
            title = BookValidator.validate_text(title)
            found = False

            for book in self.__books:
                if title.lower() == book.title.lower():
                    print(book.get_info())
                    print("-" * 40)
                    found = True

            if not found:
               print("Book not found.")
        except ValueError as e:
            print(e)





