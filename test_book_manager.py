
import pytest
from book import Book, PrintedBook, EBook
from validation import BookValidator
from manager import BookManager
from storage import BookStorage

class TestBook:
    def test_book_creation(self):
        book = Book("1984", "George Orwell", 1949)

        assert book.title == "1984"
        assert book.author == "George Orwell"
        assert book.year == 1949

    def test_printed_book(self):
        book = PrintedBook("1984", "George Orwell", 1949)

        assert isinstance (book, Book)
        assert "Printed Book" in book.get_info()    

    def test_ebook(self):
        book = EBook("Animal Farm", "George Orwell", 1945, "PDF")

        assert isinstance(book, Book)
        assert book.format == "PDF"
        assert "EBook" in book.get_info()

class TestBookValidator:
    def test_validate_text(self):
        assert BookValidator.validate_text("   animal farm   ") == "Animal Farm"

    def test_empty_text(self):
        with pytest.raises(ValueError): 
            BookValidator.validate_text("   ")

    def test_validate_year(self):
        assert BookValidator.validate_year("1949") == 1949

    def test_ivalid_year(self):
        with pytest.raises(ValueError): 
            BookValidator.validate_year("abc")

    def test_future_year(self):
        with pytest.raises(ValueError): 
            BookValidator.validate_year("3000")

    def test_negative_year(self):
        with pytest.raises(ValueError): 
            BookValidator.validate_year("-1949")

    def test_validate_book_type(self):
        assert BookValidator.validate_book_type("Printed Book") == "printed book"

    def test_invalid_book_type(self):
        with pytest.raises(ValueError):
            BookValidator.validate_book_type("audio book")

    def test_valid_format(self):
        assert BookValidator.validate_format("pdf") == "PDF"

    def test_invalid_format(self):
        with pytest.raises(ValueError):
            BookValidator.validate_format("PDS")

class TestBookManager:
    @pytest.fixture
    def manager(self, tmp_path):
        filename = str(tmp_path / "test_books.json")
        return BookManager(filename)

    def test_add_book(self, manager):
        manager.add_book("1984", "George Orwell", 1949, "printed book")

        books = manager.storage.load_books()

        assert len(books) == 1
        assert books[0].title == "1984"
        assert isinstance(books[0], PrintedBook)

    def test_add_ebook(self, manager):
        manager.add_book("Animal Farm", "George Orwell", 1945, "ebook", "PDF")

        books = manager.storage.load_books()

        assert len(books) == 1
        assert isinstance(books[0], EBook)
        assert books[0].format == "PDF"

    def test_add_invalid_book(self, manager):
        manager.add_book("1984", "George Orwell", 3000, "printed book")

        books = manager.storage.load_books()

        assert len(books) == 0
        







