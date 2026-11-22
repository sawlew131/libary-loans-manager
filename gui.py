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


def main():
    root = tk.Tk()
    LibraryGUI(root, Library())
    root.mainloop()


if __name__ == "__main__":
    main()
