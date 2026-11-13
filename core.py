# core.py - The Brain - No input(), No Tkinter here

class Book:
    def __init__(self, book_id, title, author, copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.copies = copies

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
            return True
        return False
    
    def return_book(self,book_id):
        if book_id not in self.loans:
            return False
        book = self.find(book_id)
        book.copies += 1
        del self.loans[book_id]
        return True
    
    def show_all(self):
        books = []
        self._inorder(self.root, books)
        return books

    def _inorder(self, node, books):
        if node is not None:
            self._inorder(node.left, books)
            books.append(node.book)
            self._inorder(node.right, books)