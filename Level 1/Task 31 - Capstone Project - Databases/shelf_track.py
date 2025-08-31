import sqlite3

def setup_tables(cursor):
    """Create the author and book tables if they don't exist."""
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS author (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            country TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            authorID INTEGER NOT NULL,
            qty INTEGER NOT NULL,
            FOREIGN KEY (authorID) REFERENCES author(id)
        )
    ''')

def insert_initial_data(cursor, conn):
    """Insert initial authors and books if tables are empty."""
    authors = [
        (1290, "Charles Dickens", "England"),
        (8937, "J.K. Rowling", "England"),
        (2356, "C.S. Lewis", "Ireland"),
        (6380, "J.R.R. Tolkien", "South Africa"),
        (5620, "Lewis Carroll", "England")
    ]
    books = [
        (3001, "A Tale of Two Cities", 1290, 30),
        (3002, "Harry Potter and the Philosopher’s Stone", 8937, 40),
        (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
        (3004, "The Lord of the Rings", 6380, 37),
        (3005, "Alice’s Adventures in Wonderland", 5620, 12)
    ]

    try:
        cursor.execute("SELECT COUNT(*) FROM author")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO author VALUES (?, ?, ?)", authors)
            conn.commit()
    except sqlite3.Error as e:
        print("Could not insert authors:", e)

    try:
        cursor.execute("SELECT COUNT(*) FROM book")
        if cursor.fetchone()[0] == 0:
            cursor.executemany("INSERT INTO book VALUES (?, ?, ?, ?)", books)
            conn.commit()
    except sqlite3.Error as e:
        print("Could not insert books:", e)

def get_int(prompt, length=4):
    """Ask for an integer of a given digit length. Retry or cancel."""
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
            if len(str(val)) != length:
                raise ValueError(f"Needs to be {length} digits.")
            return val
        except ValueError as e:
            print("Invalid input:", e)
            again = input("Try again? (y to retry): ").strip().lower()
            if again != "y":
                return None

def enter_book(cursor, conn):
    """Add a new book, validating IDs before inserting."""
    print("\n--- Add New Book ---")

    while True:
        book_id = get_int("Enter new book ID (4 digits): ")
        if book_id is None:
            print("Cancelled.")
            return
        cursor.execute("SELECT 1 FROM book WHERE id = ?", (book_id,))
        if cursor.fetchone():
            print("That book ID already exists.")
            again = input("Try different ID? (y to retry): ").strip().lower()
            if again != "y":
                return
        else:
            break

    title = input("Enter title: ").strip()
    if not title:
        print("No title entered.")
        return

    while True:
        author_id = get_int("Enter author ID (4 digits): ")
        if author_id is None:
            print("Cancelled.")
            return
        cursor.execute("SELECT 1 FROM author WHERE id = ?", (author_id,))
        if not cursor.fetchone():
            print("That author ID does not exist.")
            again = input("Try another? (y to retry): ").strip().lower()
            if again != "y":
                return
        else:
            break

    try:
        qty = int(input("Enter quantity: ").strip())
        if qty < 0:
            raise ValueError("Quantity cannot be negative.")
    except ValueError as e:
        print("Invalid quantity:", e)
        return

    try:
        cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?)", (book_id, title, author_id, qty))
        conn.commit()
        print("Book added.")
    except sqlite3.Error as e:
        print("Could not add book:", e)

def update_book(cursor, conn):
    """Update a book's title, quantity, or author ID."""
    print("\n--- Update Book ---")
    book_id = get_int("Enter book ID to update: ")
    if book_id is None:
        return

    try:
        cursor.execute("""
            SELECT b.title, b.qty, b.authorID, a.name, a.country
            FROM book b
            INNER JOIN author a ON b.authorID = a.id
            WHERE b.id = ?
        """, (book_id,))
        row = cursor.fetchone()
    except sqlite3.Error as e:
        print("Could not retrieve book:", e)
        return

    if not row:
        print("Book not found.")
        return

    print(f"\nCurrent title   : {row[0]}")
    print(f"Current qty     : {row[1]}")
    print(f"Author ID       : {row[2]}")
    print(f"Author name     : {row[3]}")
    print(f"Author country  : {row[4]}")

    option = input("\nUpdate (title/qty/authorID): ").strip()
    if option not in ("title", "qty", "authorID"):
        print("Invalid option.")
        return

    new_value = input(f"Enter new value for {option}: ").strip()
    if not new_value:
        return

    if option == "qty":
        try:
            new_value = int(new_value)
            if new_value < 0:
                raise ValueError
        except ValueError:
            print("Invalid quantity.")
            return
    elif option == "authorID":
        try:
            new_value = int(new_value)
            if len(str(new_value)) != 4:
                raise ValueError
        except ValueError:
            print("Invalid author ID.")
            return
        cursor.execute("SELECT 1 FROM author WHERE id = ?", (new_value,))
        if not cursor.fetchone():
            print("Author ID does not exist.")
            return

    try:
        cursor.execute(f"UPDATE book SET {option} = ? WHERE id = ?", (new_value, book_id))
        conn.commit()
        print("Book updated.")
    except sqlite3.Error as e:
        print("Update failed:", e)

def delete_book(cursor, conn):
    """Delete a book by its ID."""
    print("\n--- Delete Book ---")
    book_id = get_int("Enter book ID to delete: ")
    if book_id is None:
        return

    try:
        cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
        conn.commit()
        if cursor.rowcount:
            print("Book deleted.")
        else:
            print("Book not found.")
    except sqlite3.Error as e:
        print("Delete failed:", e)

def search_books(cursor):
    """Search for books by title keyword."""
    print("\n--- Search Books ---")
    keyword = input("Search by title: ").strip()
    try:
        cursor.execute("SELECT id, title, authorID, qty FROM book WHERE title LIKE ?", (f"%{keyword}%",))
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        print("Search failed:", e)
        return

    if rows:
        for r in rows:
            print(f"ID: {r[0]} | Title: {r[1]} | Author ID: {r[2]} | Qty: {r[3]}")
    else:
        print("No matches found.")

def view_all_books(cursor):
    """Show all books with author and country details."""
    print("\n--- All Books (with Author & Country) ---")
    try:
        cursor.execute("""
            SELECT b.id, b.title, a.name, a.country, b.qty
            FROM book b
            INNER JOIN author a ON b.authorID = a.id
            ORDER BY b.id
        """)
        rows = cursor.fetchall()
    except sqlite3.Error as e:
        print("Could not retrieve books:", e)
        return

    if not rows:
        print("No books in the system.")
        return

    sep = "-" * 50
    for book_id, title, name, country, qty in rows:
        print(sep)
        print(f"ID      : {book_id}")
        print(f"Title   : {title}")
        print(f"Author  : {name} [{country}]")
        print(f"Quantity: {qty}")
    print(sep)

def main():
    """Main menu loop."""
    with sqlite3.connect("ebookstore.db") as conn:
        cursor = conn.cursor()
        setup_tables(cursor)
        insert_initial_data(cursor, conn)

        while True:
            print("\n--- Shelf Track Menu ---")
            print("1. Enter book")
            print("2. Update book")
            print("3. Delete book")
            print("4. Search books")
            print("5. View details of all books (with author + country)")
            print("0. Exit")

            choice = input("Choose an option: ").strip()

            if choice == '1':
                enter_book(cursor, conn)
            elif choice == '2':
                update_book(cursor, conn)
            elif choice == '3':
                delete_book(cursor, conn)
            elif choice == '4':
                search_books(cursor)
            elif choice == '5':
                view_all_books(cursor)
            elif choice == '0':
                print("Exiting...")
                break
            else:
                print("Not a valid choice.")

if __name__ == "__main__":
    main()
