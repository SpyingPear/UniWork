import sqlite3
def connect_db():
    # Opens a database connection and returns cursor + connection
    conn = sqlite3.connect("ebookstore.db")
    return conn, conn.cursor()

def setup_tables(cursor):
    # Creates book and author tables if they don't exist yet
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
    # Populates the tables with default data (once-off)
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

    cursor.execute("SELECT COUNT(*) FROM author")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO author VALUES (?, ?, ?)", authors)

    cursor.execute("SELECT COUNT(*) FROM book")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO book VALUES (?, ?, ?, ?)", books)

    conn.commit()

# ------------------ CORE FUNCTIONS ------------------

def get_int(prompt, length=4):
    # Asks for an integer input and checks it's the right length
    try:
        val = int(input(prompt))
        if len(str(val)) != length:
            raise ValueError(f"Must be exactly {length} digits.")
        return val
    except ValueError as e:
        print("Invalid input:", e)
        return None

def enter_book(cursor, conn):
    print("\n--- Add New Book ---")
    id = get_int("Enter new book ID (4 digits): ")
    if id is None:
        return
    title = input("Enter title: ")
    authorID = get_int("Enter author ID (4 digits): ")
    if authorID is None:
        return
    try:
        qty = int(input("Enter quantity: "))
        cursor.execute("INSERT INTO book VALUES (?, ?, ?, ?)", (id, title, authorID, qty))
        conn.commit()
        print("Book added.")
    except sqlite3.IntegrityError:
        print("Book ID or Author ID not found or already exists.")
    except Exception as e:
        print("Error:", e)

def update_book(cursor, conn):
    print("\n--- Update Book ---")
    id = get_int("Enter book ID to update: ")
    if id is None:
        return

    cursor.execute('''
        SELECT book.title, book.qty, author.name, author.country
        FROM book
        INNER JOIN author ON book.authorID = author.id
        WHERE book.id = ?
    ''', (id,))
    result = cursor.fetchone()

    if not result:
        print("Book not found.")
        return

    print(f"Current title: {result[0]}")
    print(f"Current quantity: {result[1]}")
    print(f"Author: {result[2]} ({result[3]})")

    option = input("Update (title/qty/authorID): ").strip()
    if option not in ("title", "qty", "authorID"):
        print("Invalid field.")
        return

    value = input(f"New value for {option}: ").strip()
    try:
        if option in ("qty", "authorID"):
            value = int(value)
        cursor.execute(f"UPDATE book SET {option} = ? WHERE id = ?", (value, id))
        conn.commit()
        print("Book updated.")
    except Exception as e:
        print("Update failed:", e)

def delete_book(cursor, conn):
    print("\n--- Delete Book ---")
    id = get_int("Enter book ID: ")
    if id is None:
        return
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    print("Book deleted." if cursor.rowcount else "Book not found.")

def search_books(cursor):
    print("\n--- Search Books ---")
    keyword = input("Enter title keyword: ").strip()
    cursor.execute("SELECT * FROM book WHERE title LIKE ?", ('%' + keyword + '%',))
    results = cursor.fetchall()
    if results:
        for book in results:
            print(f"ID: {book[0]} | Title: {book[1]} | Author ID: {book[2]} | Qty: {book[3]}")
    else:
        print("No matches found.")

def view_all_books(cursor):
    print("\n--- Book Details ---")
    cursor.execute('''
        SELECT book.title, author.name, author.country
        FROM book
        INNER JOIN author ON book.authorID = author.id
    ''')
    rows = cursor.fetchall()
    if not rows:
        print("No books available.")
        return
    for title, author, country in rows:
        print(f"\nTitle: {title}")
        print(f"Author: {author}")
        print(f"Country: {country}")
        print("-" * 40)

# ------------------ MAIN MENU ------------------

def main():
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
            print("5. View details of all books")
            print("0. Exit")

            choice = input("Select option: ").strip()

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
                print("Exiting program...")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
