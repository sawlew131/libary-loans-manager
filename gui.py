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
        ttk.Button(top, text="Search", command=self.do_search).pack(side="left")
        ttk.Button(top, text="Clear", command=self.clear_search).pack(side="left", padx=(3, 0))

        # --- Middle: book list ---
        middle = ttk.Frame(root, padding=(10, 0, 10, 10))
        middle.pack(fill="both", expand=True)

        columns = ("title", "author", "status", "borrower", "due")
        self.tree = ttk.Treeview(middle, columns=columns, show="headings")
        self.tree.heading("title", text="Title")
        self.tree.heading("author", text="Author")
        self.tree.heading("status", text="Status")
        self.tree.heading("borrower", text="Borrower")
        self.tree.heading("due", text = "Due Date")
        self.tree.column("title", width=250)
        self.tree.column("author", width=150)
        self.tree.column("status", width=100)
        self.tree.column("borrower", width=150)
        self.tree.pack(fill="both", expand=True)
        self.tree.tag_configure("overdue", background="red", foreground="white")

        # --- Bottom: buttons ---
        bottom = ttk.Frame(root, padding=10)
        bottom.pack(fill="x")

        ttk.Button(bottom, text="Add Book", command=self.add_book).pack(side="left", padx=3)
        ttk.Button(bottom, text="Borrow", command=self.borrow_book).pack(side="left", padx=3)
        ttk.Button(bottom, text="Return", command=self.return_book).pack(side="left", padx=3)
        ttk.Button(bottom, text="Delete", command=self.delete_book).pack(side="left", padx=3)

        self.refresh()

    def refresh(self, filter_text=""):
        for item in self.tree.get_children():
            self.tree.delete(item)
        filter_text = filter_text.lower().strip()
        for book in self.lib.show_all():
            if filter_text and filter_text not in book.title.lower() and filter_text not in book.author.lower():
                continue
            borrower = self.lib.loans.get(book.id, "")
            status = "Borrowed" if book.id in self.lib.loans else f"Available ({book.copies})"
            due = self.lib.get_due_date(book.id)
            if self.lib.is_overdue(book.id):
                status = "OVERDUE"
                due = due + " - OVERDUE"
            tag = ("overdue",) if status == "OVERDUE" else ()
            self.tree.insert("", "end", iid=str(book.id), values=(book.title, book.author, status, borrower, due), tags=tag)
    def do_search(self):
        self.refresh(self.search_var.get())

    def clear_search(self):
        self.search_var.set("")
        self.refresh()

    def _get_selected_id(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No book selected", "Click a book in the table first.", parent=self.root)
            return None
        return int(selected[0])

    def add_book(self):
        book_id = simpledialog.askinteger("Add Book", "Book ID (a number):", parent=self.root)
        if book_id is None:
            return
        title = simpledialog.askstring("Add Book", "Title:", parent=self.root)
        if not title:
            return
        author = simpledialog.askstring("Add Book", "Author:", parent=self.root)
        if not author:
            return
        copies = simpledialog.askinteger("Add Book", "How many copies?", parent=self.root, minvalue=1)
        if copies is None:
            return
        self.lib.insert(Book(book_id, title, author, copies))
        self.refresh()

    def borrow_book(self):
        book_id = self._get_selected_id()
        if book_id is None:
            return
        borrower = simpledialog.askstring("Borrow Book", "Borrower name:", parent=self.root)
        if not borrower:
            return
        if self.lib.borrow_book(book_id, borrower):
            self.refresh()
        else:
            messagebox.showerror("Cannot borrow", "No copies available.", parent=self.root)

    def return_book(self):
        book_id = self._get_selected_id()
        if book_id is None:
            return
        if self.lib.return_book(book_id):
            self.refresh()
        else:
            messagebox.showerror("Cannot return", "That book is not on loan.", parent=self.root)

    def delete_book(self):
        book_id = self._get_selected_id()
        if book_id is None:
            return
        if messagebox.askyesno("Delete Book", "Delete this book?", parent=self.root):
            self.lib.delete_book(book_id)
            self.refresh()

def main():
    root = tk.Tk()
    lib = Library()
    lib.load_from_file()
    gui = LibraryGUI(root, lib)

    def on_close():
        lib.save_to_file()
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()

if __name__ == "__main__":
        main()
