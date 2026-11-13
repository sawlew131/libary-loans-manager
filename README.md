# Library Loans Manager

A small library system in Python using a Binary Search Tree (BST).

Books are stored sorted by ID, so listing and finding books is fast.

## Features
- Add books with ID, title, author, copies
- Borrow a book (decreases copies, tracks borrower)
- Return a book (increases copies)
- List all books in sorted ID order

## Run it
python cli.py

## Run tests
python -m pytest -v