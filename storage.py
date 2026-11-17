#Class for saving and loading book dfata.

import json
from book import Book, PrintedBook, EBook

class BookStorage:
    def __init__(self, filename: str = "books.json") -> None:
        self.filename = filename

    #Load book data from JSON file.
    def load_books(self) -> list[Book]:
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Book Collection file not found")
            return []
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON file format.")
        except OSError:
            raise OSError("Unable to read book collection")

        books: list[Book] =[]

        for item in data:
            book : Book
            if item["book_type"] == "printed book":
                book = PrintedBook(
                    item["title"],
                    item["author"],
                    item["year"]
                )
            elif item["book_type"] == "ebook":
                book = EBook(
                    item["title"],
                    item["author"],
                    item["year"],
                    item["file_format"]
                )
            else:
                raise ValueError("Invalid book type in JSON file")

            books.append(book)

        return books

    #Save book data to the JSON file.
    def save_books(self, books: list[Book]):
        data = []

        for book in books:
            item = {
                "title": book.title,
                "author": book.author,
                "year":book.year
            }

            if isinstance(book, PrintedBook):
                item["book_type"] = "printed book"
            elif isinstance(book, EBook):
                item["book_type"] = "ebook"
                item["file_format"] = book.format
            else:
                raise ValueError("Invalid book type")
            
            data.append(item)

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent= 4, ensure_ascii= False) 
        except OSError:
            raise OSError("Unable to save book collection.")



