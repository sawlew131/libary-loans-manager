# Library Loans Manager

A small library system in Python using a Binary Search Tree (BST).

Books are stored sorted by ID, so listing and finding books is fast.

## Features

- Add books with ID, title, author, copies
- Borrow a book (decreases copies, tracks borrower)
- Return a book (increases copies)
- Search for a book by ID or title
- Delete a book
- List all books in sorted ID order
- Save and load books from `library.json`

## Run it

GUI (main app): 
py gui.py
CLI(terminal version):
py cli.py


## Run tests 
python -m pytest -v


## Files

- `core.py` - Book and Library logic (BST, borrow/return, save/load)
- `gui.py` - Tkinter GUI
- `cli.py` - Terminal version
- `test_core.py` - Tests for core logic


