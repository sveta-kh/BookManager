#Validate and normalize book data
from datetime import datetime

class BookValidator:
     #Validate and normalize book title and author.
    @staticmethod
    def validate_text(text: str):
        word = text.split()
        text =" ".join(word)
        text = text.title()
        if not text:
            raise ValueError("This field cannot be empty")
        
        return text

    #Validate and normalize book publishing year.
    @staticmethod
    def validate_year(year: str | int) -> int:
        try:
            valid__year = int(year)
        except ValueError:
            raise ValueError("Please enter the year as a whole number.")
        if valid__year <= 0 or valid__year > datetime.now().year:
            raise ValueError("Please enter a valid publication year")
        
        return valid__year

    #Validate book type.
    @staticmethod
    def validate_book_type(book_type: str):
        book_type = book_type.strip().lower()
        valid_type = ["printed book", "ebook"]
        if book_type not in valid_type:
            raise ValueError("Please select a valid book type")
        
        return book_type

    #Validate the ebook file format.
    @staticmethod
    def validate_format(file_format: str):
        file_format = file_format.strip().upper()
        valid_formats =["PDF", "EPUB", "MOBI", "AZW3"]
        if file_format not in valid_formats:
            raise ValueError("Please enter a valid format")

        return file_format
