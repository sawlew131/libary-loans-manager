from core import Library, Book

lib = Library()

def show_help():
    print("\nCommands:")
    print("  add <id> <title> <author> <copies>")
    print("  list")
    print("  find <id>")
    print("  borrow <id> <name>")
    print("  return <id>")
    print("  help")
    print("  quit")

print("Library Loans Manager - type 'help'")
show_help()

while True:
    raw = input("\n> ").strip()
    if not raw:
        continue

    parts = raw.split()
    cmd = parts[0].lower()

    if cmd == "quit":
        print("Bye!")
        break

    elif cmd == "help":
        show_help()

    elif cmd == "add":
        # add 1 Dune Herbert 2
        try:
            book_id = int(parts[1])
            copies = int(parts[4])
            book = Book(book_id, parts[2], parts[3], copies)
            lib.insert(book)
            print(f"Added {parts[2]}")
        except:
            print("Use: add <id> <title> <author> <copies>")

    elif cmd == "list":
        books = lib.show_all()
        if not books:
            print("No books yet")
        for b in books:
            print(f"{b.id} - {b.title} by {b.author} ({b.copies} left)")

    elif cmd == "find":
        book = lib.find(int(parts[1]))
        if book:
            print(f"{book.id} - {book.title} by {book.author} ({book.copies} left)")
        else:
            print("Not found")

    elif cmd == "borrow":
        ok = lib.borrow_book(int(parts[1]), parts[2])
        print("Borrowed!" if ok else "Can't borrow - not found or no copies")

    elif cmd == "return":
        ok = lib.return_book(int(parts[1]))
        print("Returned!" if ok else "Can't return - not on loan")

    else:
        print("Unknown command - type 'help'")
    