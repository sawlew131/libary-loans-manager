# gui.py - Tkinter front end for the Library Loans Manager
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

from core import Book, Library

class LibraryGUI:
    def __init__(self, root, library):
        self.root = root
        self.lib = library
        self.root.title("Library Loans Manager")
        self.root.geometry("760x520")
        self.root.minsize(620, 420)

        # --- Top: search bar ---
        top = ttk.Frame(root, padding=10)
        top.pack(fill="x")

        ttk.Label(top, text="Search:").pack(side="left")
        self.search_var = tk.StringVar()
        ttk.Entry(top, textvariable=self.search_var).pack(side="left", fill="x", expand=True, padx=(5, 5))
        ttk.Button(top, text="Search").pack(side="left")

        # --- Middle: book list ---
        middle = ttk.Frame(root, padding=(10, 0, 10, 10))
        middle.pack(fill="both", expand=True)

        columns = ("title", "author", "status", "borrower")
        self.tree = ttk.Treeview(middle, columns=columns, show="headings")
        self.tree.heading("title", text="Title")
        self.tree.heading("author", text="Author")
        self.tree.heading("status", text="Status")
        self.tree.heading("borrower", text="Borrower")
        self.tree.column("title", width=250)
        self.tree.column("author", width=150)
        self.tree.column("status", width=100)
        self.tree.column("borrower", width=150)
        self.tree.pack(fill="both", expand=True)

        # --- Bottom: buttons ---
        bottom = ttk.Frame(root, padding=10)
        bottom.pack(fill="x")

        ttk.Button(bottom, text="Add Book").pack(side="left", padx=3)
        ttk.Button(bottom, text="Borrow").pack(side="left", padx=3)
        ttk.Button(bottom, text="Return").pack(side="left", padx=3)
        ttk.Button(bottom, text="Delete").pack(side="left", padx=3)

def main():
    root = tk.Tk()
    LibraryGUI(root, Library())
    root.mainloop()

if __name__ == "__main__":
    main()