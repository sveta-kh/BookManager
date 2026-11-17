#Class representing a book and its attributes.

class Book:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    #Return book information.
    def get_info(self):
        return f"Book Information:\nTitle: {self.title}\nAuthor: {self.author}\nYear: {self.year}"

#Child class representing a printed book.    
class PrintedBook(Book):
    def get_info(self):
        return super().get_info() + "\nType: Printed Book"

#Child class representing an EBook.
class EBook(Book):
    def __init__(self, title: str, author: str, year: int, format: str) -> None:
        super().__init__(title, author, year) 
        self.format = format 

    def get_info(self):
        return super().get_info() + f"\nType: EBook\nFormat: {self.format}"     

