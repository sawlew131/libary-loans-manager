# core.py - The Brain - No input(), no Tkinter here
class Book:
    def __init__(self, book_id, title, author,copies):
        self.id = book_id
        self.title = title
        self.author = author
        self.copies = copies
class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None
class Library:
    def __init__(self):
        self.root = None
    def insert(self, book):
        pass
    def find(self,book_id):
        pass
    def show_all(self):
        pass