from core import Book, Library

def test_insert_keeps_books_sorted():
    lib = Library()
    lib.insert(Book(5, "Book Five", "Author", 1))
    lib.insert(Book(1, "Book One", "Author", 1))
    lib.insert(Book(2, "Book Two", "Author", 1))
    ids = [book.id for book in lib.show_all()]
    assert ids == [1, 2, 5]

def test_borrow_decreases_copies():
    lib = Library()
    lib.insert(Book(2, "Book Two", "Author", 2))
    assert lib.borrow_book(2, "Sam") is True
    assert lib.borrow_book(2, "Alex") is True
    assert lib.borrow_book(2, "Kim") is False
    assert lib.find(2).copies == 0

def test_return_increases_copies():
    lib = Library()
    lib.insert(Book(2, "Book Two", "Author", 1))
    assert lib.borrow_book(2, "Sam") is True
    assert lib.find(2).copies == 0
    assert lib.return_book(2) is True
    assert lib.find(2).copies == 1
    assert lib.borrow_book(2, "Sam") is True
    