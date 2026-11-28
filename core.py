# core.py - The Brain - No input(), No Tkinter here
import json
import os
from datetime import date, datetime, timedelta

class Book:
    def __init__(self, book_id, title, author, copies, available=None):
        self.id = book_id
        self.title = title
        self.author = author
        self.copies = copies
        self.available = copies if available is None else available

    def __str__(self):
        return f"{self.id} | {self.title} by {self.author} | Copies: {self.copies}"

class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

class Library:
    def __init__(self):
        self.root = None
        self.loans = {}
        self.due_dates = {}
    def insert(self, book):
        # Public method - calls the private helper
        self.root = self._insert(self.root, book)
    def _insert(self, node, book):
        if node is None:
            return Node(book)
        if book.id < node.book.id:
            node.left = self._insert(node.left, book)
        elif book.id > node.book.id:
            node.right = self._insert(node.right, book)
        else:
            # Same ID - just update copies
            node.book.copies = book.copies
        return node

    def find(self, book_id):
        node = self.root
        while node is not None:
            if book_id == node.book.id:
                return node.book
            elif book_id < node.book.id:
                node = node.left
            else:
                node = node.right
        return None
    
    def borrow_book(self, book_id, borrower):
        book = self.find(book_id)
        if book is None:
            return False
        if book.copies > 0:
            book.copies -=1
            self.loans[book_id] = borrower
            self.due_dates[book_id] = (date.today() + timedelta(days=14)). isoformat()
            return True
        return False
    
    def return_book(self, book_id):
        if book_id not in self.loans:
            return False
        book = self.find(book_id)
        book.copies += 1
        del self.loans[book_id]
        if book_id in self.due_dates:
            del self.due_dates[book_id]
        return True

    def get_due_date(self, book_id):
        return self.due_dates.get(book_id, "")

    def is_overdue(self, book_id):
        due = self.due_dates.get(book_id)
        if not due:
            return False
        return date.fromisoformat(due) < date.today()

    def show_all(self):
        books = []
        self._inorder(self.root, books)
        return books

    def _inorder(self, node, books):
        if node is not None:
            self._inorder(node.left, books)
            books.append(node.book)
            self._inorder(node.right, books)

    def delete_book(self, book_id):
        # Rebuild the tree without this book - simplest safe BST delete
        remaining = [b for b in self.show_all() if b.id != book_id]
        if len(remaining) == len(self.show_all()):
            return False
        self.root = None
        self.loans.pop(book_id, None)
        self.due_dates.pop(book_id, None)
        for book in remaining:
            self.insert(book)
        return True

    def save_to_file(self, filename="library.json"):
        data = []
        for b in self.show_all():
            data.append({
                "id": b.id,
                "title": b.title,
                "author": b.author,
                "copies": b.copies,
                "available": getattr(b, "available", b.copies)
            })
        with open(filename, "w") as f:
            json.dump({"books": data, "loans": self.loans, "due_dates": self.due_dates}, f, indent=2)

    def load_from_file(self, filename="library.json"):
        if not os.path.exists(filename):
            return
        with open(filename) as f:
            data = json.load(f)
        self.root = None
        self.loans = {int(k): v for k, v in data.get("loans", {}).items()}
        self.due_dates = {int(k): v for k, v in data.get("due_dates", {}).items()}
        for d in data.get("books", []):
            book = Book(d["id"], d["title"], d["author"], d["copies"], d.get("available"))
            self.insert(book)
