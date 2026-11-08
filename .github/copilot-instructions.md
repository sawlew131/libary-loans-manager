# Library Loans Manager

## Project overview

This is a small Python library-loans manager. Business logic belongs in `core.py` and must remain separate from user input and GUI code.

The current model has:

- `Book`: stores an ID, title, author, and available copy count.
- `Node`: stores a `Book` and left/right children in a binary search tree.
- `Library`: owns the BST root and implements operations that are currently stubs.

## Coding conventions

- Keep the implementation in standard Python with no third-party dependencies.
- Preserve the separation described by the heading in `core.py`: no `input()`, Tkinter, printing, or other presentation concerns in core business logic.
- Use `book.id` as the BST key unless an implementation requirement explicitly changes that contract.
- Follow the surrounding code's simple, compact class-oriented style.
- Make focused changes; do not add a CLI, GUI, persistence layer, or dependencies unless requested.

## Core TODOs

Implement these methods in `Library` when working on the core:

- `insert(book)`: add a book to the BST in ID order without losing the existing tree.
- `find(book_id)`: locate and return the matching book, or an appropriate absent value if it is not found.
- `show_all()`: traverse and return books in ascending ID order.

## Validation

There is currently no automated test suite. When Python code changes, at minimum run:

```powershell
python -m compileall core.py
```

Prefer adding focused standard-library tests when implementing behaviors, and run the narrowest relevant test command before broader validation.
